# -*- coding: utf-8 -*-
from setuptools import setup, Command


name = "suitable"
description = "Suitable is a thin wrapper around the Ansible API."


def get_long_description():
    for line in open('README.rst').readlines():
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
    version='0.3',
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
        'ansible'
    ],
    extras_require={
        'tests': [
            'pytest',
        ]
    },
    cmdclass={
        'test': PyTest
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
