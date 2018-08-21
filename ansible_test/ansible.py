"""
Handles ansible files
"""
from os import path

from jinja2 import Template
from pkg_resources import resource_string

from config import ANSIBLE_TESTDIR


def generate_inventory(options):
    """
    Generate inventory file based on jinja2 template
    """
    rendered_inventory_file = Template(
        resource_string('ansible_test',
                        'templates/inventory.yml.j2'
                       ).render(options)
    )
    with open(path.join(ANSIBLE_TESTDIR,
                        'inventory.yml'), 'wb') as inventory_file:
        inventory_file.write(rendered_inventory_file)


def generate_playbook(options):
    """
    Generate playbook file based on jinja2 template
    """
    rendered_playbook_file = Template(
        resource_string('ansible_test',
                        'templates/playbook.yml.j2'
                       ).render(options)
    )
    with open(path.join(ANSIBLE_TESTDIR,
                        'playbook.yml'), 'wb') as playbook_file:
        playbook_file.write(rendered_playbook_file)


def execute_playbook():
    """
    """
    # TODO
    print("TODO")


def syntax_check():
    """
    """
    # TODO
    print("TODO")
