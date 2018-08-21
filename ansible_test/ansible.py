"""
Handles ansible files
"""
import ansible

from os import path

from jinja2 import Template
from pkg_resources import resource_string

from config import ANSIBLE_TESTDIR

from ansible.errors import AnsibleOptionsError, AnsibleError
from ansible.playbook import Play

def generate_files(filename, context):
    """
    Generate ansible files
    """
    file_path = path.join(ANSIBLE_TESTDIR,
                          "{}.yml".format(filename))

    rendered_generate_file = Template(
        resource_string('ansible_test',
                        "templates/{}.yml.j2".format(filename)
                       ).render(context)
    )
    with open(file_path, 'wb') as generate_file:
        generate_file.write(rendered_generate_file)

    return file_path


def execute_playbook():
    """
    Play ansible
    """
    # TODO
    pass
    playbook_file = generate_files('playbook', context)
    inventory_file = generate_files('inventory', context)


def syntax_check():
    """
    Check ansible syntax
    """
    # TODO
    pass
