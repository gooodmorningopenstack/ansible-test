from os import path
from jinja2 import Template
from pkg_resources import resource_string
from config import ANSIBLE_TESTDIR

def generate_inventory():
    with open(path.join(ANSIBLE_TESTDIR, "inventory.yml"), "wb") as f:
        f.write(resource_string("ansible_test", "resources/inventory.yml"))

def generate_playbook(options):
    with open(path.join(ANSIBLE_TESTDIR, "playbook.yml"), "wb") as f:
        f.write(resource_string("ansible_test", "resources/playbook.yml"))

def execute_playbook():
    # TODO
    print("TODO")

def syntax_check():
    # TODO
    print("TODO")
