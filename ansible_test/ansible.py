"""
Handles ansible files
"""
import ansible

from os import path

from jinja2 import Template
from pkg_resources import resource_string

from config import ANSIBLE_TESTDIR

import tempfile

import ansible_runner
from ansible_runner.interface import run as Runner

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

def run_playbook(private_data_dir=None, playbook=None, role=None):
    """
    """
    # test only purpose, need to be deleted
    inventory = 'localhost ansible_connection=local'
    playbook = [
      {
        'hosts': 'localhost',
        'gather_facts': True,
        'tasks': [
          {
            'debug': 'msg=Hello'
          }
        ],
      }
    ]

    playbook_file = playbook or generate_files('playbook', role_name)
    private_data_dir = private_data_dir or tempfile.mkdtemp()

    cmdline = {
      'private_data_dir': private_data_dir,
      'playbook': playbook,
      'inventory': inventory,
    }

    run_pb = Runner(**cmdline)
    return run_pb
