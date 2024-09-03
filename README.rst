.. image:: https://seantis.github.io/suitable/_static/logo.svg
    :alt: Suitable
    :width: 50%
    :align: center

An Ansible API for humans.

Documentation
-------------

`<https://seantis.github.io/suitable/>`_

Quick Start
-------------

Suitable provides a simple wrapper over Ansible's internal API, that allows you to use Ansible programmatically.

.. code-block:: pycon

    >>> from suitable import Api
    >>> api = Api('localhost')
    >>> api.command('whoami').stdout()
    'myuser'

Warning
-------

Suitable is not endorsed by Ansible and it is not affilated with it. Use at
your own peril.

The official way to use Ansible from Python is documented here:
`<http://docs.ansible.com/ansible/developing_api.html>`_

Compatibility
-------------

* Python 3.8+
* Ansible 6+
* Mitogen 0.3.7+

Support for older releases is kept only if possible. New Ansible releases
are favored over old ones.

Run Tests
---------

.. code-block:: console

    pip install tox
    tox

Build Status
------------

.. image:: https://github.com/seantis/suitable/actions/workflows/python-tox.yaml/badge.svg
    :target: https://github.com/seantis/suitable/actions
    :alt:    Tests

Test Coverage
-------------

.. image:: https://codecov.io/github/seantis/suitable/coverage.svg?branch=master
    :target: https://codecov.io/github/seantis/suitable?branch=master
    :alt: Test coverage

Latest Release
--------------

.. image:: https://badge.fury.io/py/suitable.svg
    :target: https://badge.fury.io/py/suitable
    :alt: Latest release
