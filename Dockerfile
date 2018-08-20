FROM debian:latest as ansible

ENV DEBIAN_FRONTEND="noninteractive" \
    TZ="Europe/Paris"

RUN apt-get update  -qq && \
    apt-get upgrade -qqy

RUN apt-get install -qqy --no-install-recommends \
      build-essential \
      libffi-dev \
      libssl-dev \
      python-dev \
      python-pip \
      python-setuptools \
      python-wheel && \
      apt-get clean

RUN pip install --upgrade \
      ansible \
      cryptography

FROM debian:latest

COPY --from=ansible /usr/local /usr/local

RUN apt-get update  -qq && \
    apt-get upgrade -qqy && \
    apt-get install -qqy \
      python \
      sudo \
      systemd && \
    apt-get clean

WORKDIR /etc/ansible

RUN /bin/echo -e \
      '[local]\nlocalhost ansible_connection=local' > \
      /etc/ansible/hosts

VOLUME [ "/sys/fs/cgroup" ]

HEALTHCHECK NONE
