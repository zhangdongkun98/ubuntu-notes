# Gitlab docker builder image
FROM docker:stable

ENV DOCKER_TLS_CERTDIR "/certs"

ENV DOCKER_CLI_EXPERIMENTAL enabled

ENV BUILDX_URL https://github.com/docker/buildx/releases/download/v0.5.1/buildx-v0.5.1.linux-amd64

RUN apk add --no-cache wget git bash findutils python3 python3-dev curl g++ libmagic skopeo jq

RUN mkdir -p $HOME/.docker/cli-plugins/

RUN wget -O $HOME/.docker/cli-plugins/docker-buildx $BUILDX_URL

RUN chmod a+x $HOME/.docker/cli-plugins/docker-buildx

RUN python3 -m ensurepip

RUN rm -r /usr/lib/python*/ensurepip

RUN pip3 install --upgrade pip setuptools

RUN if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

RUN if [ ! -e /usr/bin/python ]; then ln -sf /usr/bin/python3 /usr/bin/python; fi

RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

COPY pyproject.toml /root/

WORKDIR /root

RUN . $HOME/.poetry/env && poetry config virtualenvs.create false && poetry install
