#!/usr/bin/env python

import setuptools

setuptools.setup(
    name='ansible-test',
    version='1.0.1',
    description='An Ansible Testing Framework for Humans',
    url='https://github.com/nylas/ansible-test/',
    include_package_data = True,
    packages = setuptools.find_packages(),
    package_data = {
        "ansible_test": ["templates/*.j2"]
    },
    entry_points={
        'console_scripts': [
            'ansible-test=ansible_test.__main__:main',
        ],
    },
    install_requires=['Jinja2>=2.10', 'ansible>=2.6']
)
