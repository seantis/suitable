# -*- coding: utf-8 -*-
from setuptools import setup, Command


name = "suitable"
description = "Suitable is a thin wrapper around the Ansible API."


def get_long_description():
    with open('README.rst') as readme_file:
        for line in readme_file.readlines():
            if description in line:
                continue
            yield line.replace('\n', '')


class PyTest(Command):

    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys
        import subprocess
        errno = subprocess.call([sys.executable, 'runtests.py'])
        raise SystemExit(errno)


setup(
    name='suitable',
    version='0.13.0',
    url='http://github.com/seantis/suitable/',
    license='GPLv3',
    author='Denis Krienbühl',
    author_email='denis@href.ch',
    description=description,
    long_description='\n'.join(get_long_description()),
    packages=['suitable'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=[
        'ansible>=2.4.0.0'
    ],
    # Ansible does not support Python 3.0 through 3.4, so we do not either
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*',
    extras_require={
        'tests': [
            'mitogen',
            'pytest',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
