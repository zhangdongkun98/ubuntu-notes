#!/bin/bash

git clone https://github.com/bats-core/bats-core.git
cd bats-core
./install.sh /usr/local

mkdir -p /opt/bats/assert
git clone https://github.com/jasonkarns/bats-assert-1.git /opt/bats/assert
