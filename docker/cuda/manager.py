#!/usr/bin/env python3

# @author Jesus Alvarez <sw-cuda-installer@nvidia.com>

"""Container scripts template injector and pipeline trigger."""

#
# !! IMPORTANT !!
#
# Editors of this file should use https://github.com/python/black for auto formatting.
#

import re
import os
import pathlib
import logging
import logging.config
import shutil
import glob
import sys
import io
import select
import time
import json
from packaging import version

import jinja2
from jinja2 import Environment, Template
from plumbum import cli, local
from plumbum.cmd import rm, grep, cut, sort, find
import yaml
import glom
import docker
import git
import deepdiff
import requests


log = logging.getLogger()


HTTP_RETRY_ATTEMPTS = 3
HTTP_RETRY_WAIT_SECS = 30

SUPPORTED_DISTRO_LIST = ["ubuntu", "ubi", "centos"]


class Manager(cli.Application):
    """CUDA CI Manager"""

    PROGNAME = "manager.py"
    VERSION = "0.0.1"

    manifest = None
    ci = None

    manifest_path = cli.SwitchAttr(
        "--manifest",
        str,
        excludes=["--shipit-uuid"],
        help="Select a manifest to use.",
        default="manifest.yaml",
    )

    shipit_uuid = cli.SwitchAttr(
        "--shipit-uuid",
        str,
        excludes=["--manifest"],
        help="Shipit UUID used to build release candidates (internal)",
    )

    def _load_manifest_yaml(self):
        log.debug(f"Loading manifest: {self.manifest_path}")
        with open(self.manifest_path, "r") as f:
            self.manifest = yaml.load(f, yaml.Loader)

    def _load_rc_push_repos_manifest_yaml(self):
        push_repo_path = pathlib.Path("manifests/rc-push-repos.yml")
        log.debug(f"Loading push repos manifest: {push_repo_path}")
        obj = {}
        with open(push_repo_path, "r") as f:
            obj = yaml.load(f, yaml.Loader)
        return obj

    def load_ci_yaml(self):
        with open(".gitlab-ci.yml", "r") as f:
            self.ci = yaml.load(f, yaml.Loader)

    def _load_app_config(self):
        with open("manager-config.yaml", "r") as f:
            logging.config.dictConfig(yaml.safe_load(f.read())["logging"])

    # Get data from a object by dotted path. Example "cuda."v10.0".cuda_requires"
    def get_data(self, obj, *path, can_skip=False):
        try:
            data = glom.glom(obj, glom.Path(*path))
        except glom.PathAccessError:
            if can_skip:
                return
            raise glom.PathAccessError
        return data

    # Returns a unmarshalled json object
    def get_http_json(self, url):
        for attempt in range(HTTP_RETRY_ATTEMPTS):
            r = requests.get(url)
            log.debug("response status code %s", r.status_code)
            #  log.debug("response body %s", r.json())
            if r.status_code == 200:
                log.info("http json get successful")
                break
            else:
                if attempt < HTTP_RETRY_ATTEMPTS:
                    log.warning(
                        "http json get attempt failed! ({} of {})".format(
                            attempt + 1, HTTP_RETRY_ATTEMPTS
                        )
                    )
                    log.warning("Sleeping {} seconds".format(HTTP_RETRY_WAIT_SECS))
                    time.sleep(HTTP_RETRY_WAIT_SECS)
                else:
                    log.critical("Could not get shipit json!")
                    sys.exit(1)
        return r.json()

    def main(self):
        self._load_app_config()
        if not self.nested_command:  # will be ``None`` if no sub-command follows
            log.error("No subcommand given!")
            print()
            self.help()
            return 1
        elif len(self.nested_command[1]) < 2 and any(
            "generate" in arg for arg in self.nested_command[1]
        ):
            log.error(
                "Subcommand 'generate' missing  required arguments! use 'generate --help'"
            )
            return 1
        elif not any(halp in self.nested_command[1] for halp in ["-h", "--help"]):
            log.info("cuda ci manager start")
            if not self.shipit_uuid:
                self._load_manifest_yaml()


@Manager.subcommand("trigger")
class ManagerTrigger(Manager):
    DESCRIPTION = "Trigger for changes."

    repo = None

    trigger_all = False
    trigger_explicit = []

    key = ""
    pipeline_name = "default"

    CI_API_V4_URL = "https://gitlab-master.nvidia.com/api/v4"
    CI_PROJECT_ID = 12064

    dry_run = cli.Flag(
        ["-n", "--dry-run"], help="Show output but don't make any changes."
    )

    no_test = cli.Flag(["--no-test"], help="Don't run smoke tests")

    no_scan = cli.Flag(["--no-scan"], help="Don't run security scans")

    no_push = cli.Flag(["--no-push"], help="Don't push images to the registries")

    rebuildb = cli.Flag(
        ["--rebuild-builder"],
        help="Force rebuild of the builder image used to build the cuda images.",
    )

    branch = cli.SwitchAttr(
        "--branch",
        str,
        help="The branch to trigger against on Gitlab",
        default="master",
    )

    distro = cli.SwitchAttr(
        "--os-name",
        str,
        group="Targeted",
        excludes=["--manifest", "--trigger-override"],
        help="The distro name without version information",
        default=None,
    )

    distro_version = cli.SwitchAttr(
        "--os-version",
        str,
        group="Targeted",
        excludes=["--manifest", "--trigger-override"],
        help="The distro version",
        default=None,
    )

    release_label = cli.SwitchAttr(
        "--release-label",
        str,
        group="Targeted",
        excludes=["--manifest", "--trigger-override"],
        help="The cuda release label. Example: 11.2.0",
        default=None,
    )

    arch = cli.SwitchAttr(
        "--arch",
        cli.Set("x86_64", "ppc64le", "arm64", case_sensitive=False),
        group="Targeted",
        excludes=["--manifest", "--trigger-override"],
        help="Generate container scripts for a particular architecture.",
    )

    candidate_number = cli.SwitchAttr(
        "--candidate-number",
        str,
        group="Targeted",
        excludes=["--manifest", "--trigger-override"],
        help="The CUDA release candidate number.",
        default=None,
    )

    candidate_url = cli.SwitchAttr(
        "--candidate-url",
        str,
        group="Targeted",
        excludes=["--manifest", "--trigger-override"],
        help="The CUDA release candidate url.",
        default=None,
    )

    webhook_url = cli.SwitchAttr(
        "--webhook-url",
        str,
        group="Targeted",
        excludes=["--manifest", "--trigger-override"],
        help="The url to POST to when the job is done. POST will include a list of tags pushed.",
        default=None,
    )

    branch = cli.SwitchAttr(
        "--branch",
        str,
        group="Targeted",
        help="The branch to trigger against on gitlab.",
        default=None,
    )

    trigger_override = cli.SwitchAttr(
        "--trigger-override",
        str,
        excludes=["--shipit-uuid"],
        help="Override triggering from gitlab with a variable.",
        default=None,
    )

    def ci_pipeline_by_name(self, name):
        log.debug(f"have pipeline_name: {name}")
        rgx = re.compile(fr"^\s+- \$(?!all)(.*_{name}_.*) == \"true\"$")
        ci_vars = []
        with open(".gitlab-ci.yml", "r") as fp:
            for _, line in enumerate(fp):
                match = rgx.match(line)
                if match:
                    ci_vars.append(match.groups(0)[0])
        return ci_vars

    def ci_pipelines(
        self, cuda_version, distro, distro_version, arch,
    ):
        """Returns a list of pipelines extracted from the gitlab-ci.yml

        Iterates .gitlab-ci.yml line by line looking for a match on the pipeline variable.

        For example:

            - if: '$ubuntu20_04_11_1_x86_64 == "true"'

        Every pipeline has this variable defined, and that is used with the gitlab trigger api to trigger explicit
        pipelines.

        Returns a list of pipeline variables to pass to the gitlab API.

        All arguments to this function can be None, in that case all of the pipelines are returned.
        """
        if cuda_version:
            distro_list_by_cuda_version = self.supported_distro_list_by_cuda_version(
                version
            )
            log.debug(f"distro_list_by_cuda_version: {distro_list_by_cuda_version}")

        log.debug(
            "version: '%s' distro: '%s' distro_version: '%s' arch: '%s'"
            % (cuda_version, distro or "any", distro_version or "any", arch or "any")
        )

        if not arch:
            arch = "(x86_64|arm64|ppc64le)"
        if not cuda_version:
            cuda_version = "(\d{1,2}_\d{1,2}_?\d?)"
        if not distro:
            distro = "(ubuntu\d{2}_\d{2})?(?(2)|([a-z]*\d))"
        elif not distro_version:
            distro = f"({distro}\d)"
            if "ubuntu" in distro:
                distro = "(ubuntu\d{2}_\d{2})"
        else:
            distro = f"{distro}{distro_version}"

        # Full match regex without known cuda version with distro and distro version in one group
        #  ^\s+- if: '\$((ubuntu)?(?(2)(\d{2}_\d{2})|([a-z]*)(\d))_(\d{1,2}_\d{1,2}_?\d?)_(x86_64|arm64|ppc64le))\s+==\s.true.'$

        # Full match regex without known cuda version and distro and distro version in separate groups
        #  ^\s+- if: '\$((ubuntu\d{2}_\d{2})?(?(2)|([a-z]*\d))_(\d{1,2}_\d{1,2}_?\d?)_(x86_64|arm64|ppc64le))\s+==\s.true.'$

        rgx_temp = fr"^\s+- if: '\$({distro}_{cuda_version}_{arch})\s+==\s.true.'$"
        log.debug(f"regex_matcher: {rgx_temp}")
        rgx = re.compile(rgx_temp)
        ci_vars = []
        with open(".gitlab-ci.yml", "r") as fp:
            for _, line in enumerate(fp):
                match = rgx.match(line)
                if match:
                    ci_vars.append(match.groups(0)[0])
        return ci_vars

    def get_cuda_version_from_trigger(self, trigger):
        rgx = re.compile(r".*cuda-?([\d\.]+).*$")
        match = rgx.match(trigger)
        if (match := rgx.match(trigger)) is not None:
            return match.group(1)
        else:
            log.info(f"Cuda version not found in trigger!")

    def get_pipeline_name_from_trigger(self, trigger):
        rgx = re.compile(r".*name:(\w+)$")
        if (match := rgx.match(trigger)) is not None:
            return match.group(1)

    def get_distro_version_from_trigger(self, trigger):
        rgx = re.compile(r".*cuda([\d\.]+).*$")
        match = rgx.match(trigger)
        if match is not None:
            return match.group(1)
        else:
            log.warning(f"Could not extract version from trigger: '{trigger}'!")

    def supported_distro_list_by_cuda_version(self, version):
        if not version:
            return
        distros = ["ubuntu", "ubi", "centos"]
        keys = self.parent.manifest[self.key].keys()

        # There are other keys in the cuda field other than distros, we need to strip those out
        def get_distro_name(name):
            r = re.compile("[a-zA-Z]+")
            return r.findall(name)[0]

        return [f for f in keys if get_distro_name(f) in distros]

    def check_explicit_trigger(self):
        """Checks for a pipeline trigger command and builds a list of pipelines to trigger.

        Checks for a trigger command in the following order:

        - git commit message
        - trigger_override command line flag

        Returns True if pipelines have been found matching the trigger command.
        """
        self.repo = git.Repo(pathlib.Path("."))
        commit = self.repo.commit("HEAD")
        rgx = re.compile(r"ci\.trigger = (.*)")
        log.debug("Commit message: %s", repr(commit.message))

        if self.trigger_override:
            log.info("Using trigger override!")
            pipeline = self.trigger_override
        else:
            match = rgx.search(commit.message)
            if not match:
                log.debug("No explicit trigger found in commit message.")
                return False
            else:
                log.info("Explicit trigger found in commit message")
                pipeline = match.groups(0)[0].lower()

        if "all" in pipeline:
            log.info("Triggering ALL of the jobs!")
            self.trigger_all = True
            return True
        else:
            jobs = []
            jobs.append(pipeline)
            log.debug(f"jobs: {jobs}")

            if "," in pipeline:
                jobs = [x.strip() for x in pipeline.split(",")]

            for job in jobs:
                version = self.get_cuda_version_from_trigger(job)
                if not version:
                    self.pipeline_name = self.get_pipeline_name_from_trigger(job)

                log.debug("cuda_version: %s" % version)
                log.debug("pipeline_name: %s" % self.pipeline_name)

                self.key = f"cuda_v{version}"
                if self.pipeline_name != "default":
                    self.key = f"cuda_v{version}_{self.pipeline_name}"

                distro = next((d for d in SUPPORTED_DISTRO_LIST if d in job), None)
                distro_version = None
                if distro:
                    # The trigger specifies a distro
                    assert not any(  # distro should not contain digits
                        char.isdigit() for char in distro
                    )
                    distro_version = (
                        re.match(f"^.*{distro}([\d\.]*)", job).groups(0)[0] or None
                    )

                arch = next(
                    (arch for arch in ["x86_64", "ppc64le", "arm64"] if arch in job),
                    None,
                )

                log.debug(
                    f"job: '{job}' name: '{self.pipeline_name}' version: '{version}' distro: '{distro}' distro_version: '{distro_version}' arch: '{arch}'"
                )

                # Any or all of the variables passed to this function can be None
                for cvar in self.ci_pipelines(version, distro, distro_version, arch):
                    if not cvar in self.trigger_explicit:
                        log.info("Triggering '%s'", cvar)
                        self.trigger_explicit.append(cvar)

            return True

    def kickoff(self):
        url = os.getenv("CI_API_V4_URL") or self.CI_API_V4_URL
        project_id = os.getenv("CI_PROJECT_ID") or self.CI_PROJECT_ID
        dry_run = os.getenv("DRY_RUN") or self.dry_run
        no_test = os.getenv("NO_TEST") or self.no_test
        no_scan = os.getenv("NO_SCAN") or self.no_scan
        no_push = os.getenv("NO_PUSH") or self.no_push
        rebuildb = os.getenv("REBUILD_BUILDER") or self.rebuildb
        token = os.getenv("CI_JOB_TOKEN")
        if not token:
            log.warning("CI_JOB_TOKEN is unset!")
        ref = os.getenv("CI_COMMIT_REF_NAME") or self.branch
        payload = {"token": token, "ref": ref, "variables[TRIGGER]": "true"}
        if self.trigger_all:
            payload["variables[all]"] = "true"
        elif self.trigger_explicit:
            for job in self.trigger_explicit:
                payload[f"variables[{job}]"] = "true"
        if no_scan:
            payload[f"variables[NO_SCAN]"] = "true"
        if no_test:
            payload[f"variables[NO_TEST]"] = "true"
        if no_push:
            payload[f"variables[NO_PUSH]"] = "true"
        if rebuildb:
            payload[f"variables[REBUILD_BUILDER]"] = "true"
        final_url = f"{url}/projects/{project_id}/trigger/pipeline"
        log.info("url %s", final_url)
        log.info("payload %s", payload)
        if not self.dry_run:
            r = requests.post(final_url, data=payload)
            log.debug("response status code %s", r.status_code)
            log.debug("response body %s", r.json())
        else:
            log.info("In dry-run mode so not making gitlab trigger POST")

    def kickoff_from_kitmaker(self):
        url = os.getenv("CI_API_V4_URL") or self.CI_API_V4_URL
        project_id = os.getenv("CI_PROJECT_ID") or self.CI_PROJECT_ID
        dry_run = os.getenv("DRY_RUN") or self.dry_run
        no_test = os.getenv("NO_TEST") or self.no_test
        no_scan = os.getenv("NO_SCAN") or self.no_scan
        no_push = os.getenv("NO_PUSH") or self.no_push
        token = os.getenv("CI_JOB_TOKEN")
        if not token:
            log.warning("CI_JOB_TOKEN is unset!")
        ref = os.getenv("CI_COMMIT_REF_NAME") or self.branch
        payload = {"token": token, "ref": self.branch, "variables[KITMAKER]": "true"}
        if no_scan:
            payload[f"variables[NO_SCAN]"] = "true"
        if no_test:
            payload[f"variables[NO_TEST]"] = "true"
        if no_push:
            payload[f"variables[NO_PUSH]"] = "true"
        payload[f"variables[TRIGGER]"] = "true"
        payload[f"variables[OS]"] = f"{self.distro}{self.distro_version}"
        payload[f"variables[OS_NAME]"] = self.distro
        payload[f"variables[OS_VERSION]"] = self.distro_version
        payload[f"variables[ARCH]"] = self.arch
        payload[f"variables[RELEASE_LABEL]"] = self.release_label
        payload[f"variables[IMAGE_TAG_SUFFIX]"] = f"-{self.candidate_number}"
        payload[f"variables[CANDIDATE_URL]"] = self.candidate_url
        payload[f"variables[WEBHOOK_URL]"] = self.webhook_url

        final_url = f"{url}/projects/{project_id}/trigger/pipeline"
        log.info("url %s", final_url)
        masked_payload = payload.copy()
        masked_payload["token"] = "[ MASKED ]"
        log.info("payload %s", masked_payload)

        if not self.dry_run:
            r = requests.post(final_url, data=payload)
            log.debug("response status code %s", r.status_code)
            log.debug("response body %s", r.json())
        else:
            log.info("In dry-run mode so not making gitlab trigger POST")

    def main(self):
        if self.dry_run:
            log.info("Dryrun mode enabled. Not making changes")

        if self.parent.shipit_uuid:
            # Make sure all of our arguments are present
            if any(
                [
                    not i
                    for i in [
                        self.arch,
                        self.release_label,
                        self.distro,
                        self.distro_version,
                        self.candidate_number,
                        self.candidate_url,
                        self.webhook_url,
                        self.branch,
                    ]
                ]
            ):
                # Plumbum doesn't allow this check
                log.error(
                    """Missing arguments (one or all): ["--arch", "--cuda-version", "--os", "--os-version", "--candidate-number"]"""
                )
                sys.exit(1)
            log.debug("Triggering gitlab kitmaker pipeline using shipit source")
            self.kickoff_from_kitmaker()
        else:
            self.check_explicit_trigger()
            if self.trigger_all or self.trigger_explicit:
                self.kickoff()


@Manager.subcommand("push")
class ManagerContainerPush(Manager):
    DESCRIPTION = "Login and push to the container registries"

    image_name = cli.SwitchAttr(
        "--image-name", str, help="The image name to tag", default="", mandatory=True
    )

    distro = cli.SwitchAttr(
        "--os-name", str, help="The distro to use.", default=None, mandatory=True
    )

    distro_version = cli.SwitchAttr(
        "--os-version", str, help="The distro version", default=None, mandatory=True
    )

    dry_run = cli.Flag(["-n", "--dry-run"], help="Show output but don't do anything!")

    cuda_version = cli.SwitchAttr(
        "--cuda-version",
        str,
        help="The cuda version to use. Example: '10.1'",
        default=None,
        mandatory=True,
    )

    image_tag_suffix = cli.SwitchAttr(
        "--tag-suffix",
        str,
        help="The suffix to append to the tag name. Example 10.1-base-centos6<suffix>",
        default="",
    )

    arch = cli.SwitchAttr(
        "--arch",
        cli.Set("x86_64", "ppc64le", "arm64", case_sensitive=False),
        requires=["--image-name", "--os-name", "--os-version", "--cuda-version"],
        help="Push images for a particular architecture.",
    )

    pipeline_name = cli.SwitchAttr(
        "--pipeline-name",
        str,
        help="The name of the pipeline the deploy is coming from",
    )

    tag_manifest = cli.SwitchAttr("--tag-manifest", str, help="A list of tags to push",)

    client = None
    repos = []
    tags = []
    key = ""
    copy_failed = False
    repo_creds = {}

    def setup_repos(self):
        distro_push_repos = self.get_data(
            self.parent.manifest,
            self.key,
            f"{self.distro}{self.distro_version}",
            "push_repos",
        )
        excluded_repos = self.get_data(
            self.parent.manifest,
            self.key,
            f"{self.distro}{self.distro_version}",
            self.arch,
            "exclude_repos",
            can_skip=True,
        )

        for repo, metadata in self.parent.manifest["push_repos"].items():
            if "gitlab-master" in repo:
                # Images have already been pushed to gitlab by this point
                log.debug(f"Skipping push to {repo}")
                continue
            if metadata.get("only_if", False) and not os.getenv(metadata["only_if"]):
                log.info("repo: '%s' only_if requirement not satisfied", repo)
                continue
            if distro_push_repos and repo not in distro_push_repos:
                log.info("repo: '%s' is excluded for this image", repo)
                continue
            if excluded_repos and repo in excluded_repos:
                log.info("repo: '%s' is excluded for this image", repo)
                continue
            if self.arch not in metadata["registry"]:
                log.debug(f"{repo} does not contain an entry for {self.arch}")
                continue
            creds = False
            user = os.getenv(metadata["user"])
            if not user:
                user = metadata["user"]
            passwd = os.getenv(metadata["pass"])
            if not passwd:
                passwd = metadata["pass"]
            registry = metadata["registry"][self.arch]
            self.repo_creds[registry] = {"user": user, "pass": passwd}
            self.repos.append(registry)
        if not self.repos:
            log.fatal(
                "Could not retrieve container image repo credentials. Environment not set?"
            )
            sys.exit(1)

    # Args is a tuple
    def skopeocmd(self, args):
        skop = local["/usr/bin/skopeo"]
        (pipe_r, pipe_w) = os.pipe()
        p = skop.popen(args=args, shell=False, stdout=pipe_w, stderr=pipe_w)
        while p.poll() is None:
            # Loop long as the selct mechanism indicates there
            # is data to be read from the buffer
            while len(select.select([pipe_r], [], [], 0)[0]) == 1:
                log.debug(os.read(pipe_r, 8192).decode("utf-8").strip())
        os.close(pipe_r)
        os.close(pipe_w)
        if p.returncode != 0:
            log.error("See log output...")
            return False
        return True

    def push_images(self):
        with open(self.tag_manifest) as f:
            tags = f.readlines()
        stags = [x.strip() for x in tags]
        for tag in stags:
            if not tag:
                continue
            log.info("Processing image: %s:%s", self.image_name, tag)
            for repo in self.repos:
                log.info("COPYING to: %s:%s", repo, tag)
                if self.dry_run:
                    log.debug("dry-run; not copying")
                    continue
                for attempt in range(HTTP_RETRY_ATTEMPTS):
                    if self.skopeocmd(
                        (
                            "copy",
                            "--src-creds",
                            "{}:{}".format(
                                "gitlab-ci-token", os.getenv("CI_JOB_TOKEN")
                            ),
                            "--dest-creds",
                            "{}:{}".format(
                                self.repo_creds[repo]["user"],
                                self.repo_creds[repo]["pass"],
                            ),
                            f"docker://{self.image_name}:{tag}",
                            f"docker://{repo}:{tag}",
                        )
                    ):
                        log.info("Copy was successful")
                        break
                    else:
                        if attempt < HTTP_RETRY_ATTEMPTS:
                            log.warning(
                                "Copy Attempt failed! ({} of {})".format(
                                    attempt + 1, HTTP_RETRY_ATTEMPTS
                                )
                            )
                            log.warning(
                                "Sleeping {} seconds".format(HTTP_RETRY_WAIT_SECS)
                            )
                            time.sleep(HTTP_RETRY_WAIT_SECS)
                        else:
                            log.warning("Copy failed!")
                            self.copy_failed = True

    def main(self):
        log.debug("dry-run: %s", self.dry_run)
        self.key = f"cuda_v{self.cuda_version}"
        if self.pipeline_name:
            self.key = f"cuda_v{self.cuda_version}_{self.pipeline_name}"
        self.client = docker.DockerClient(
            base_url="unix://var/run/docker.sock", timeout=600
        )
        self.setup_repos()
        self.push_images()
        if self.copy_failed:
            log.error("Errors were encountered copying images!")
            sys.exit(1)
        log.info("Done")


@Manager.subcommand("generate")
class ManagerGenerate(Manager):
    DESCRIPTION = "Generate Dockerfiles from templates."

    cuda = {}
    dist_base_path = None  # pathlib object. The parent "base" path of output_path.
    output_manifest_path = None  # pathlib object. The path to save the shipit manifest.
    output_path = {}  # The product of parsing the input templates
    key = ""
    cuda_version_is_release_label = False

    template_env = Environment(
        extensions=["jinja2.ext.do"], trim_blocks=True, lstrip_blocks=True
    )

    generate_ci = cli.Flag(["--ci"], help="Generate the gitlab pipelines only.",)

    generate_all = cli.Flag(["--all"], help="Generate all of the templates.",)

    distro = cli.SwitchAttr(
        "--os-name",
        str,
        group="Targeted",
        excludes=["--all"],
        help="The distro to use.",
        default=None,
    )

    distro_version = cli.SwitchAttr(
        "--os-version",
        str,
        group="Targeted",
        excludes=["--all"],
        help="The distro version",
        default=None,
    )

    cuda_version = cli.SwitchAttr(
        "--cuda-version",
        str,
        excludes=["--all"],
        group="Targeted",
        help="[DEPRECATED for newer cuda versions!] The cuda version to use. Example: '11.2'",
        default=None,
    )

    release_label = cli.SwitchAttr(
        "--release-label",
        str,
        excludes=["--all"],
        group="Targeted",
        help="The cuda version to use. Example: '11.2.0'",
        default=None,
    )

    arch = cli.SwitchAttr(
        "--arch",
        cli.Set("x86_64", "ppc64le", "arm64", case_sensitive=False),
        excludes=["--all"],
        group="Targeted",
        help="Generate container scripts for a particular architecture.",
    )

    pipeline_name = cli.SwitchAttr(
        "--pipeline-name",
        str,
        excludes=["--all"],
        group="Targeted",
        help="Use a pipeline name for manifest matching.",
        default="default",
    )

    def supported_distro_list_by_cuda_version(self, version):
        if not version:
            return
        distros = ["ubuntu", "ubi", "centos"]
        keys = self.parent.manifest[self.key].keys()

        # There are other keys in the cuda field other than distros, we need to strip those out
        def get_distro_name(name):
            r = re.compile("[a-zA-Z]+")
            return r.findall(name)[0]

        return [f for f in keys if get_distro_name(f) in distros]

    def supported_arch_list(self):
        ls = []
        for k in glom.glom(
            self.parent.manifest,
            glom.Path(self.key, f"{self.distro}{self.distro_version}"),
        ):
            if k in ["x86_64", "ppc64le", "arm64"]:
                ls.append(k)
        return ls

    def cudnn_versions(self):
        obj = []
        for k, v in self.cuda["components"].items():
            if k.startswith("cudnn") and v:
                obj.append(k)
        return obj

    # extracts arbitrary keys and inserts them into the templating context
    def extract_keys(self, val):
        rgx = re.compile(r"^v\d+\.\d")
        for k, v in val.items():
            if rgx.match(k):
                # Do not copy cuda version keys
                continue
            # These top level keys should be ignored since they are processed elsewhere
            if k in [
                "exclude_repos",
                "build_version",
                "components",
                *self.supported_arch_list(),
                *self.supported_distro_list_by_cuda_version(
                    self.cuda_version or self.release_label
                ),
            ]:
                continue
            self.cuda[k] = v

    # For cudnn templates, we need a custom template context
    def output_cudnn_template(self, cudnn_version_name, input_template, output_path):
        cudnn_manifest = self.cuda["components"][cudnn_version_name]
        if "source" in cudnn_manifest:
            cudnn_manifest["basename"] = os.path.basename(cudnn_manifest["source"])
            cudnn_manifest["dev"]["basename"] = os.path.basename(
                cudnn_manifest["dev"]["source"]
            )

        new_ctx = {
            "cudnn": self.cuda["components"][cudnn_version_name],
            "arch": self.arch,
            "version": self.cuda["version"],
            "image_tag_suffix": self.cuda["image_tag_suffix"],
            "os": self.cuda["os"],
        }
        log.debug("cudnn template context: %s", new_ctx)
        self.output_template(
            input_template=input_template, output_path=output_path, ctx=new_ctx
        )

    def output_template(self, input_template, output_path, ctx=None):
        ctx = ctx if ctx is not None else self.cuda
        with open(input_template) as f:
            log.debug("Processing template %s", input_template)
            new_output_path = pathlib.Path(output_path)
            extension = ".j2"
            name = input_template.name
            if "dockerfile" in input_template.name.lower():
                new_filename = "Dockerfile"
            elif ".jinja" in str(input_template):
                extension = ".jinja"
                new_filename = (
                    name[: -len(extension)] if name.endswith(extension) else name
                )
            else:
                new_filename = (
                    name[len("base-") : -len(extension)]
                    if name.startswith("base-") and name.endswith(extension)
                    else name
                )
            template = self.template_env.from_string(f.read())
            if not new_output_path.exists():
                log.debug(f"Creating {new_output_path}")
                new_output_path.mkdir(parents=True)
            log.info(f"Writing {new_output_path}/{new_filename}")
            with open(f"{new_output_path}/{new_filename}", "w") as f2:
                f2.write(template.render(cuda=ctx))

    def prepare_context(self):
        # checks the cudnn components and ensures at least one is installed from the public "machine-learning" repo
        def use_ml_repo():
            use_ml_repo = False
            # First check the manifest to see if a ml repo url is specified
            if not self.get_data(
                self.parent.manifest,
                self.key,
                f"{self.distro}{self.distro_version}",
                self.arch,
                "ml_repo_url",
                can_skip=True,
            ):
                return use_ml_repo
            # if a cudnn component contains "source", then it is installed from a different source than the public machine
            # learning repo
            # If any of the cudnn components lack the source key, then the ML repo should be used
            for comp, val in self.cuda["components"].items():
                if next(
                    (True for mlcomp in ["cudnn", "nccl"] if mlcomp in comp), False
                ):
                    if val and "source" not in val:
                        use_ml_repo = True
            return use_ml_repo

        conf = self.parent.manifest
        if self.release_label:
            major = self.release_label.split(".")[0]
            minor = self.release_label.split(".")[1]
        else:
            major = self.cuda_version.split(".")[0]
            minor = self.cuda_version.split(".")[1]

        self.image_tag_suffix = self.get_data(
            conf,
            self.key,
            f"{self.distro}{self.distro_version}",
            "image_tag_suffix",
            can_skip=True,
        )
        if not self.image_tag_suffix:
            self.image_tag_suffix = ""

        # Only set in version < 11.0
        build_version = self.get_data(
            conf,
            self.key,
            f"{self.distro}{self.distro_version}",
            self.arch,
            "components",
            "build_version",
            can_skip=True,
        )
        legacy_release_label = None
        if build_version:
            legacy_release_label = f"{self.cuda_version}.{build_version}"
        log.debug(f"build_version: {build_version}")

        # The templating context. This data structure is used to fill the templates.
        self.cuda = {
            "use_ml_repo": False,
            "version": {
                "release_label": self.cuda_version
                if self.cuda_version_is_release_label
                else (self.release_label or legacy_release_label),
                "major": major,
                "minor": minor,
                "major_minor": f"{major}.{minor}",
            },
            "os": {"distro": self.distro, "version": self.distro_version},
            "arch": self.arch,
            "image_tag_suffix": self.image_tag_suffix,
            "components": self.get_data(
                conf,
                self.key,
                f"{self.distro}{self.distro_version}",
                self.arch,
                "components",
            ),
        }
        self.cuda["use_ml_repo"] = use_ml_repo()

        # Users of manifest.yaml are allowed to set arbitrary keys for inclusion in the templates
        # and the discovered keys are injected into the template context.
        # We only checks at three levels in the manifest
        self.extract_keys(
            self.get_data(conf, self.key, f"{self.distro}{self.distro_version}",)
        )
        self.extract_keys(
            self.get_data(
                conf, self.key, f"{self.distro}{self.distro_version}", self.arch,
            )
        )
        log.debug("template context %s" % (self.cuda))
        #  sys.exit(1)

    def generate_cudnn_scripts(self, base_image, input_template):
        for pkg in self.cudnn_versions():
            self.cuda["components"][pkg]["target"] = base_image
            self.output_cudnn_template(
                cudnn_version_name=pkg,
                input_template=pathlib.Path(input_template),
                output_path=pathlib.Path(f"{self.output_path}/{base_image}/{pkg}"),
            )

    # CUDA 8 uses a deprecated image layout
    def generate_containerscripts_cuda_8(self):
        for img in ["devel", "runtime"]:
            base = img
            if img == "runtime":
                # for CUDA 8, runtime == base
                base = "base"
            temp_path = self.cuda["template_path"]
            log.debug("temp_path: %s, output_path: %s", temp_path, self.output_path)
            self.output_template(
                input_template=pathlib.Path(f"{temp_path}/{base}/Dockerfile.jinja"),
                output_path=pathlib.Path(f"{self.output_path}/{img}"),
            )
            # We need files in the base directory
            for filename in pathlib.Path(f"{temp_path}/{base}").glob("*"):
                if "Dockerfile" in filename.name:
                    continue
                log.debug("Checking %s", filename)
                if ".jinja" in filename.name:
                    self.output_template(filename, f"{self.output_path}/{img}")
                else:
                    log.info(f"Copying {filename} to {self.output_path}/{img}")
                    shutil.copy(filename, f"{self.output_path}/{img}")
            # cudnn image
            self.generate_cudnn_scripts(img, f"{temp_path}/cudnn/Dockerfile.jinja")

    def generate_containerscripts(self):
        for img in ["base", "devel", "runtime"]:
            self.cuda["target"] = img

            globber = f"*"
            if "legacy" in self.cuda["template_path"]:
                temp_path = pathlib.Path(self.cuda["template_path"], img)
                cudnn_template_path = pathlib.Path(
                    self.cuda["template_path"], f"cudnn/Dockerfile.jinja"
                )
                input_template = f"{temp_path}/Dockerfile.jinja"
            else:
                temp_path = pathlib.Path(self.cuda["template_path"])
                input_template = pathlib.Path(temp_path, f"{img}-dockerfile.j2")
                cudnn_template_path = pathlib.Path(temp_path, "cudnn-dockerfile.j2")
                globber = f"{img}-*"

            log.debug(
                "template_path: %s, output_path: %s", temp_path, self.output_path,
            )

            self.output_template(
                input_template=pathlib.Path(input_template),
                output_path=pathlib.Path(f"{self.output_path}/{img}"),
            )

            # copy files
            log.debug(f"temp_path: {temp_path} img: {img}")
            for filename in pathlib.Path(temp_path).glob(globber):
                if "dockerfile" in filename.name.lower():
                    continue
                #  log.debug("Checking %s", filename)
                if not self.cuda["use_ml_repo"] and "nvidia-ml" in str(filename):
                    continue
                if any(f in filename.name for f in [".j2", ".jinja"]):
                    self.output_template(filename, f"{self.output_path}/{img}")

            # cudnn image
            if "base" not in img:
                self.generate_cudnn_scripts(img, cudnn_template_path)

    # FIXME: Probably a much nicer way to do this with GLOM...
    # FIXME: Turn off black auto format for this function...
    # fmt: off
    def generate_gitlab_pipelines(self):

        manifest = self.parent.manifest
        ctx = {"manifest_path": self.parent.manifest_path}

        def get_cudnn_components(key, distro, arch):
            comps = {}
            for comp, val in manifest[key][distro][arch]["components"].items():
                if "cudnn" in comp and val:
                    #  print(comp, val)
                    comps[comp] = {}
                    comps[comp]["version"] = val["version"]
            return comps

        def matched(key):
            match = rgx.match(k)
            if match:
                return match

        for k, _ in manifest.items():
            rgx = re.compile(r"cuda_v([\d\.]+)(?:_(\w+))?$")
            if (match := matched(k)) is None:
                log.debug("No match for %s" % k)
                continue

            log.info("Adding pipeline '%s'" % k)
            cuda_version = match.group(1)
            if (pipeline_name := match.group(2)) is None:
                pipeline_name = "default"
            log.debug("matched cuda_version: %s" % cuda_version)
            log.debug("matched pipeline_name: %s" % pipeline_name)

            if cuda_version not in ctx:
                ctx[cuda_version] = {}
            ctx[cuda_version][pipeline_name] = {}
            ctx[cuda_version][pipeline_name]["yaml_safe"] = cuda_version.replace(".", "_")

            key = f"cuda_v{cuda_version}"
            if pipeline_name and pipeline_name != "default":
                key = f"cuda_v{cuda_version}_{pipeline_name}"

            #  log.debug("key: '%s'" % key)
            #  log.debug("cuda_version: '%s'" % cuda_version)
            ctx[cuda_version][pipeline_name]["dist_base_path"] = self.get_data(manifest, key, "dist_base_path")
            ctx[cuda_version][pipeline_name]["pipeline_name"] = self.pipeline_name

            for distro, _ in manifest[key].items():
                dmrgx = re.compile(r"(?P<name>[a-zA-Z]+)(?P<version>[\d\.]+)$")
                if (dm := dmrgx.match(distro)) is None:
                    continue

                #  log.debug("distro: '%s'" % distro)
                #  log.debug("pipeline_name: '%s'" % pipeline_name)
                ctx[cuda_version][pipeline_name][distro] = {}
                ctx[cuda_version][pipeline_name][distro]["name"] = dm.group('name')
                ctx[cuda_version][pipeline_name][distro]["version"] = dm.group('version')
                ctx[cuda_version][pipeline_name][distro]["yaml_safe"] = distro.replace(".", "_")
                image_tag_suffix = self.get_data(manifest, key, distro, "image_tag_suffix", can_skip=True)
                ctx[cuda_version][pipeline_name][distro]["image_tag_suffix"] = ""
                ctx[cuda_version][pipeline_name][distro]["image_name"] = {}

                if image_tag_suffix:
                    ctx[cuda_version][pipeline_name][distro]["image_tag_suffix"] = image_tag_suffix

                ctx[cuda_version][pipeline_name][distro]["arches"] = []

                for arch, _ in manifest[key][distro].items():
                    if arch not in ["arm64", "ppc64le", "x86_64"]:
                        continue

                    #  log.debug("arch: '%s'" % arch)
                    no_os_suffix = self.get_data(manifest, key, distro, arch, "no_os_suffix", can_skip=True)
                    latest = self.get_data(manifest, key, distro, arch, "latest", can_skip=True)
                    ctx[cuda_version][pipeline_name][distro]["image_name"][arch] = self.get_data(manifest, key, distro, arch, "image_name")

                    if "latest" not in ctx[cuda_version][pipeline_name][distro]:
                        ctx[cuda_version][pipeline_name][distro]["latest"] = {}

                    ctx[cuda_version][pipeline_name][distro]["latest"][arch] = (True if latest else False)

                    if "no_os_suffix" not in ctx[cuda_version][pipeline_name][distro]:
                        ctx[cuda_version][pipeline_name][distro]["no_os_suffix"] = {}

                    ctx[cuda_version][pipeline_name][distro]["no_os_suffix"][arch] = (True if no_os_suffix else False)
                    ctx[cuda_version][pipeline_name][distro]["arches"].append(arch)

                    if "cudnn" not in ctx[cuda_version][pipeline_name][distro]:
                        ctx[cuda_version][pipeline_name][distro]["cudnn"] = {}

                    ctx[cuda_version][pipeline_name][distro]["cudnn"][arch] = get_cudnn_components(key, distro, arch)

        log.debug(f"ci pipline context: {ctx}")

        input_template = pathlib.Path("templates/gitlab/gitlab-ci.yml.jinja")
        with open(input_template) as f:
            log.debug("Processing template %s", input_template)
            output_path = pathlib.Path(".gitlab-ci.yml")
            template = self.template_env.from_string(f.read())
            with open(output_path, "w") as f2:
                f2.write(template.render(cuda=ctx))
        #  sys.exit(1)

    # fmt: on
    def get_shipit_funnel_json(self):
        modified_cuda_version = self.release_label.replace(".", "-")
        funnel_distro = self.distro
        if any(distro in funnel_distro for distro in ["centos", "ubi"]):
            funnel_distro = "rhel"
        modified_distro_version = self.distro_version.replace(".", "")
        modified_arch = self.arch.replace("_", "-")
        if modified_arch == "arm64":
            modified_arch = "sbsa"
        last_dot_index = self.release_label.rfind(".")
        platform_name = f"{funnel_distro}{modified_distro_version}-cuda-r{modified_cuda_version[:last_dot_index]}-linux-{modified_arch}.json"
        shipit_json = f"http://cuda-repo.nvidia.com/funnel/{self.parent.shipit_uuid}/{platform_name}"
        log.info(f"Retrieving funnel json from: {shipit_json}")
        return self.parent.get_http_json(shipit_json)

    def get_shipit_global_json(self):
        global_json = (
            f"http://cuda-repo.nvidia.com/funnel/{self.parent.shipit_uuid}/global.json"
        )
        log.info(f"Retrieving global json from: {global_json}")
        return self.parent.get_http_json(global_json)

    # Returns a list of packages used in the templates
    def template_packages(self):
        log.info(f"current directory: {os.getcwd()}")
        temp_dir = "ubuntu"
        if any(distro in self.distro for distro in ["centos", "ubi"]):
            temp_dir = "redhat"
        # sometimes the old ways are the best ways...
        cmd = (
            find[
                f"templates/{temp_dir}/",
                "-type",
                "f",
                "-iname",
                "*.j2",
                "-exec",
                "grep",
                "^{%.*set\ .*_component_version",
                "{}",
                ";",
            ]
            | cut["-f", "3", "-d", " "]
            | sort
        )
        log.debug(f"command: {cmd}")
        # When docker:stable (alpine) has python 3.9...
        #  return [x.removesuffix("_component_version") for x in cmd().splitlines()]
        return [
            x[: -len("_component_version")] if x.endswith("_component_version") else x
            for x in cmd().splitlines()
        ]

    def pkg_rel_from_package_name(self, name, version):
        rgx = re.search(fr"[\w\d-]*{version}-(\d)_?", name)
        if rgx:
            return rgx.group(1)

    def shipit_components(self, shipit_json, packages):
        components = {}

        fragments = shipit_json["fragments"]

        def fragment_by_name(name):
            name_with_hyphens = name.replace("_", "-")
            for k, v in fragments.items():
                for k2, v2 in v.items():
                    if any(x in v2["name"] for x in [name, name_with_hyphens]):
                        return v2

        for pkg in packages:
            #  log.debug(f"package: {pkg}")
            fragment = fragment_by_name(pkg)
            if not fragment:
                log.warning(f"{pkg} was not found in the fragments json!")
                continue

            name = fragment["name"]
            version = fragment["version"]

            pkg_rel = self.pkg_rel_from_package_name(name, version)
            assert pkg_rel  # should always have a value

            pkg_no_prefix = pkg[len("cuda_") :] if pkg.startswith("cuda_") else pkg

            log.debug(
                f"component: {pkg_no_prefix} version: {version} pkg_rel: {pkg_rel}"
            )

            components.update({f"{pkg_no_prefix}": {"version": f"{version}-{pkg_rel}"}})

        return components

    def kitpick_repo_url(self, global_json):
        product_name = global_json["product_name"]
        cand_number = global_json["cand_number"]
        repo_distro = self.distro
        if any(x in repo_distro for x in ["ubi", "centos"]):
            repo_distro = "rhel"
        clean_distro = "{}{}".format(repo_distro, self.distro_version.replace(".", ""))
        arch = self.arch
        if "ubuntu" in repo_distro and arch == "ppc64le":
            arch = "ppc64el"
        elif arch == "arm64":
            arch = "sbsa"
        return f"http://cuda-repo.nvidia.com/release-candidates/kitpicks/{product_name}/{self.release_label}/{cand_number}/repos/{clean_distro}/{arch}"

    def shipit_manifest(self):
        log.debug("Building the shipit manifest")
        sjson = self.get_shipit_funnel_json()
        gjson = self.get_shipit_global_json()
        #  self.release_label = gjson["rel_label"]
        log.info(f"Release label: {self.release_label}")
        pkgs = self.template_packages()
        log.debug(f"template packages: {pkgs}")
        components = self.shipit_components(sjson, pkgs)
        image_name = (
            "gitlab-master.nvidia.com:5005/cuda-installer/cuda/release-candidate/cuda"
        )
        template_path = "templates/ubuntu"
        if "ubuntu" not in self.distro:
            template_path = "templates/redhat"
        if not "x86_64" in self.arch:
            image_name = f"gitlab-master.nvidia.com:5005/cuda-installer/cuda/release-candidate/cuda-{self.arch}"
        base_image = f"{self.distro}:{self.distro_version}"
        if "ubi" in self.distro:
            base_image = (
                f"registry.access.redhat.com/ubi{self.distro_version}/ubi:latest"
            )
        self.parent.manifest = {
            f"cuda_v{self.release_label}": {
                "dist_base_path": self.dist_base_path.as_posix(),
                f"{self.distro}{self.distro_version}": {
                    "template_path": template_path,
                    "base_image": base_image,
                    "push_repos": ["artifactory"],
                    "repo_url": self.kitpick_repo_url(gjson),
                    "image_tag_suffix": f"-{gjson['cand_number']}",
                    f"{self.arch}": {
                        "image_name": image_name,
                        #  "requires": f"cuda>={self.cuda_version}",
                        "requires": "",
                        "components": components,
                    },
                },
            }
        }
        prepos = self._load_rc_push_repos_manifest_yaml()["push_repos"]
        self.parent.manifest.update({"push_repos": prepos})
        self.write_shipit_manifest(self.parent.manifest)

    def write_shipit_manifest(self, manifest):
        yaml_str = yaml.dump(manifest)
        with open(self.output_manifest_path, "w") as f:
            f.write(yaml_str)

    def set_output_path(self, target):
        self.output_path = pathlib.Path(f"{self.dist_base_path}/{target}-{self.arch}")
        if self.parent.shipit_uuid:
            if self.dist_base_path.exists:
                log.debug(f"Removing {self.dist_base_path}")
                rm["-rf", self.dist_base_path]()
            self.output_path = pathlib.Path(
                f"{self.dist_base_path}/{target}-{self.arch}"
            )
            self.output_manifest_path = pathlib.Path(
                f"{self.dist_base_path}/{target}-{self.arch}/manifest-{self.distro}-{self.distro_version}.yml"
            )
            log.debug(f"output_manifest_path: {self.output_manifest_path}")

        if self.output_path.exists:
            log.debug(f"Removing {self.output_path}")
            rm["-rf", self.output_path]()

        log.debug(f"Creating {self.output_path}")
        self.output_path.mkdir(parents=True, exist_ok=False)

    def target_all(self):
        log.debug("Generating all container scripts!")
        rgx = re.compile(
            # use regex101.com to debug with gitlab-ci.yml as the search text
            r"^(?P<distro>[a-zA-Z]*)(?P<distro_version>[\d\.]*)-v(?P<cuda_version>[\d\.]*)(?:-(?!cudnn|test|scan|deploy)(?P<pipeline_name>\w+))?-(?P<arch>arm64|ppc64le|x86_64)"
        )

        for ci_job, _ in self.parent.ci.items():
            if (match := rgx.match(ci_job)) is None:
                continue
            #  print(match.groups())
            #  continue
            self.distro = match.group("distro")
            self.distro_version = match.group("distro_version")
            self.cuda_version = match.group("cuda_version")
            if self.cuda_version.count(".") > 1:
                self.cuda_version_is_release_label = True
            self.pipeline_name = match.group("pipeline_name")
            self.arch = match.group("arch")

            log.debug("ci_job: '%s'" % ci_job)

            self.key = f"cuda_v{self.release_label}"
            if not self.release_label and self.cuda_version:
                self.key = f"cuda_v{self.cuda_version}"

            if self.pipeline_name:
                self.key = f"cuda_v{self.cuda_version}_{self.pipeline_name}"

            self.dist_base_path = pathlib.Path(
                self.parent.get_data(self.parent.manifest, self.key, "dist_base_path")
            )

            log.debug("dist_base_path: %s" % (self.dist_base_path))
            log.debug(
                "Generating distro: '%s' distro_version: '%s' cuda_version: '%s' release_label: '%s' arch: '%s'"
                % (
                    self.distro,
                    self.distro_version,
                    self.cuda_version,
                    self.release_label,
                    self.arch,
                )
            )
            self.targeted()
            self.cuda_version_is_release_label = False

        if not self.dist_base_path:
            log.error("dist_base_path not set!")

        #  sys.exit()

    def targeted(self):
        arches = []
        if not self.arch:
            arches = self.supported_arch_list()
        else:
            arches = [self.arch]
        for arch in arches:
            self.arch = arch
            if not self.generate_all:
                # FIXME: No need to go through this again if coming from target_all
                log.debug(
                    "Have distro: '%s' version: '%s' arch: '%s' cuda: '%s' pipeline: '%s'",
                    self.distro,
                    self.distro_version,
                    self.arch,
                    self.cuda_version or self.release_label,
                    self.pipeline_name,
                )
                self.key = f"cuda_v{self.release_label}"
                if not self.release_label and self.cuda_version:
                    self.key = f"cuda_v{self.cuda_version}"
                if self.pipeline_name and self.pipeline_name != "default":
                    self.key = f"cuda_v{self.release_label}_{self.pipeline_name}"

            self.dist_base_path = pathlib.Path(
                self.parent.get_data(
                    self.parent.manifest, self.key, "dist_base_path", can_skip=False,
                )
            )
            if not self.output_manifest_path:
                self.set_output_path(f"{self.distro}{self.distro_version}")
            self.prepare_context()

            if self.cuda_version == "8.0":
                self.generate_containerscripts_cuda_8()
            else:
                self.generate_containerscripts()

    def main(self):
        if self.parent.shipit_uuid:
            log.debug("Have shippit source, generating manifest and scripts")
            self.dist_base_path = pathlib.Path("kitpick")
            self.set_output_path(f"{self.distro}{self.distro_version}")
            self.shipit_manifest()
            self.targeted()
        else:
            self.generate_gitlab_pipelines()
            if not self.generate_ci:
                self.parent.load_ci_yaml()
                if self.generate_all:
                    self.target_all()
                else:
                    self.targeted()
        log.info("Done")


if __name__ == "__main__":
    Manager.run()
