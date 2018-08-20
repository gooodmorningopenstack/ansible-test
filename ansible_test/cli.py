#!/usr/bin/env python

import argparse
import os
import ansible
import docker

from config import ANSIBLE_TESTDIR, CONTAINER_BASE_IMAGE

def main():
    if not os.path.exists(ANSIBLE_TESTDIR):
        os.mkdir(ANSIBLE_TESTDIR)

    parser = argparse.ArgumentParser(prog="ansible-test")
    parser.add_argument("role", help="Ansible role name to test")
    parser.add_argument('--version', action='version',
                        version='%(prog)s 1.0.0')
    parser.add_argument('--docker',
                        action='store_true',
                        help="run ansible-test inside a docker container")
    parser.add_argument("--docker-image", "-i",
                        default=CONTAINER_BASE_IMAGE,
                        help="base image for docker build (default : %(default)s)")

    args, extra_args = parser.parse_known_args()

    options = {
        'role': args.role,
        'docker': args.docker,
        'docker_image': args.docker_image,
        'extra_args': extra_args
    }
    # print(args, extra_args)

    if docker:
        docker.generate_dockerfile(options)
        docker.build_container()
        docker.run_container()
    else:
        ansible.generate_inventory()
        ansible.generate_playbook(options)


if __name__ == "__main__":
    main()
