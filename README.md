[![Circle CI](https://circleci.com/gh/codeworksio/docker-speedtest.svg?style=shield "CircleCI")](https://circleci.com/gh/codeworksio/docker-speedtest)&nbsp;[![Size](https://images.microbadger.com/badges/image/codeworksio/speedtest.svg)](http://microbadger.com/images/codeworksio/speedtest)&nbsp;[![Version](https://images.microbadger.com/badges/version/codeworksio/speedtest.svg)](http://microbadger.com/images/codeworksio/speedtest)&nbsp;[![Commit](https://images.microbadger.com/badges/commit/codeworksio/speedtest.svg)](http://microbadger.com/images/codeworksio/speedtest)&nbsp;[![Docker Hub](https://img.shields.io/docker/pulls/codeworksio/speedtest.svg)](https://hub.docker.com/r/codeworksio/speedtest/)

Docker Speedtest
================

Test internet bandwidth using speedtest.net.

Installation
------------

Builds of the image are available on [Docker Hub](https://hub.docker.com/r/codeworksio/speedtest/) where you can download from the latest stable image.

    docker pull codeworksio/speedtest

Alternatively you can build the image yourself.

    docker build --tag codeworksio/speedtest \
        github.com/codeworksio/docker-speedtest

Quickstart
----------

Start container using:

    docker run --detach --restart always \
        --name speedtest \
        --hostname speedtest \
        codeworksio/speedtest
