import os

CONTAINER_NAME = "ansible-test"
CONTAINER_BASE_IMAGE = "debian:latest"
ANSIBLE_TESTDIR = os.path.join(os.getcwd(), ".ansible_test")
