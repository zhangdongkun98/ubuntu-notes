FROM carla-prerequisites:0.9.8

ARG GIT_BRANCH

USER root

# RUN apt-get update ; \
#   add-apt-repository ppa:~mhier/libboost-latest && \
#   apt-get update ; \
#   apt-get install -y ccache libboost1.73-dev libbz2-dev

RUN apt-get update ; \
  apt-get install -y ccache libboost-all-dev libbz2-dev


USER ue4

ENV HTTP_PROXY="socks5://127.0.0.1:1080"
ENV HTTPS_PROXY="socks5://127.0.0.1:1080"

WORKDIR /home/ue4/summit


