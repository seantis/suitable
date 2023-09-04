.. image:: https://cdn.jsdelivr.net/gh/seantis/suitable@master/docs/source/_static/logo.svg
    :alt: Suitable
    :width: 50%
    :align: center

An Ansible API for humans.

Documentation
-------------

`<http://suitable.readthedocs.org>`_

Warning
-------

Suitable is not endorsed by Ansible and it is not affilated with it. Use at
your own peril.

The official way to use Ansible from Python is documented here:
`<http://docs.ansible.com/ansible/developing_api.html>`_

Compatibility
-------------

* Python 3.8+
* Ansible 2.4+
* Mitogen 0.2.6+ (currently incompatible with Ansible 2.8)

Support for older releases is kept only if possible. New Ansible releases
are favored over old ones.

Run Tests
---------

.. code-block:: python

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

Changelog
---------
0.18.0 (2023-09-04)
~~~~~~~~~~~~~~~~~~~
Modernizes project structure [strfx]:

- Drops support for Python < 3.8

- Switches to `pyproject.toml`

- Moves code to source directory `src/`

- Sets up Github Actions

- Checks code with bugbear and bandit (including pre-commit hooks)

0.17.3 (2023-07-13)
~~~~~~~~~~~~~~~~~~~

- Keeps `ansible-core` dependency at 2.13.x. mitogen does not yet support any version above that
  (`see also <https://github.com/mitogen-hq/mitogen/blob/v0.3.4/ansible_mitogen/loaders.py#L52>`_).
  [strfx]

0.17.2 (2020-01-14)
~~~~~~~~~~~~~~~~~~~

- Accepts all kinds of iterables in the Inventory class, not just a limited set.
  [href]

0.17.1 (2019-10-24)
~~~~~~~~~~~~~~~~~~~

- Adds success flag to results.
  [jokurz]

0.17.0 (2019-10-14)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to connect to multiple hosts through a bastion host.
  [jokurz]

- Adds the ability to define host-specific variables.
  [jokurz]

0.16.2 (2019-10-01)
~~~~~~~~~~~~~~~~~~~

- Supports non-python Ansible modules.
  [jokurz]

0.16.1 (2019-08-19)
~~~~~~~~~~~~~~~~~~~

- Adds support for Ansible 2.8 with Mitogen 0.2.8.

  Mitogen now supports Ansible 2.8. This Suitable release requires both the
  latest Ansible 2.8 and Mitogen 0.2.8 releases.

  [href]

0.16.0 (2019-05-17)
~~~~~~~~~~~~~~~~~~~

- Adds compatibility with Ansible 2.8.

  See https://github.com/seantis/suitable/issues/27 for more information.

  Note that Mitogen 0.2.6 is not compatible with Ansible 2.8. Using it will
  raise an error. To keep using Mitogen, wait for a new release or use
  Ansible 2.7 instead.

  [href]

0.15.0 (2019-02-01)
~~~~~~~~~~~~~~~~~~~

- Adds 'host_key_checking' flag, to easily disable host key checking on
  both the vanilla Api and the Mitogen flavour.
  [href]

0.14.0 (2018-08-17)
~~~~~~~~~~~~~~~~~~~

- Adds support for dictionaries and lists in arguments.
  [href]

0.13.0 (2018-07-30)
~~~~~~~~~~~~~~~~~~~

- Adds mitogen support.
  [href]

0.12.0 (2018-06-14)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to define custom strategies and strategy plugins.
  [href]

- Activates full verbose output of Ansible when 'debug' verbosity is set.
  [href]

- Demotes the 'took ... to complete' log from info to debug.
  [href]

0.11.2 (2018-05-01)
~~~~~~~~~~~~~~~~~~~

- Fixes servers with custom ports raising a ValueError when unreachable.
  [href]

0.11.1 (2018-04-27)
~~~~~~~~~~~~~~~~~~~

- Fixes Ansible warnings showing up for no reason.
  [href]

0.11.0 (2018-04-27)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to specify the port for each server.
  [href]

0.10.1 (2018-02-19)
~~~~~~~~~~~~~~~~~~~

- Adds support for Ansible 2.5.
  [href]

0.10.0 (2017-11-14)
~~~~~~~~~~~~~~~~~~~

- Adds the ability to specify environment variables.
  [href]

0.9.0 (2017-09-19)
~~~~~~~~~~~~~~~~~~~

- Adds support for Ansible 2.4. Since this release introduces many changes
  under the hood support for Ansible 2.3 has been dropped!

  You might want to assume that this will stay this way. Older Ansible
  releases are supported if possible, but it's not a goal of this project.
  [href]

- Explicitly drops support for Python 3.0 - 3.4. Suitable supports the same
  Python versions Ansible supports, which excludes these 3.x releases.

  Supported are therefore Python 2.7, 3.5 and 3.6+.
  [href]

0.8.1 (2017-08-10)
~~~~~~~~~~~~~~~~~~~

- Adds support for Ansible's extra_vars.
  [Liuyanglong]

0.8.0 (2017-06-02)
~~~~~~~~~~~~~~~~~~~

- Adds support for Python 3.3+. Since Python 3 support in Ansible is
  experimental, only the latest Ansible (2.3+) is henceforth supported.
  [href]

0.7.4 (2017-01-27)
~~~~~~~~~~~~~~~~~~~

- Fixes an issue with Ansible 2.1.4.0. Host lists are now passed to Ansible in
  a format it expects.
  [href]

0.7.3 (2016-03-08)
~~~~~~~~~~~~~~~~~~~

- Gets password based ssh authentication working again.
  [href]

0.7.2 (2016-01-15)
~~~~~~~~~~~~~~~~~~~

- Stops command and shell modules from chocking on certain commands.
  Workaround for https://github.com/ansible/ansible/issues/13862
  [href]

0.7.1 (2016-01-15)
~~~~~~~~~~~~~~~~~~~

- Removes global state lingering around with Ansible 2.0.0.2, which introduced
  a hosts cache leading to Suitable's api instances to not be independent.
  [href]

0.7.0 (2016-01-13)
~~~~~~~~~~~~~~~~~~~

- Adds support for Ansible 2.0. **Does not support 1.x anymore!!**
  [href]

0.6 (2015-06-22)
~~~~~~~~~~~~~~~~

- Adds backwards-compatible support for Ansible 1.9. The same code running on
  suitable for Ansible 1.8 should now work with Ansible 1.9.
  [href]

0.5 (2014-11-28)
~~~~~~~~~~~~~~~~

- Adds support for Ansible 1.8.
  [href]

- Includes automated tests for Ansible versions 1.5 through 1.8.
  [href]

- Properly escapes spaces in key-value pairs. Fixes #3.
  [href]

0.4 (2014-09-05)
~~~~~~~~~~~~~~~~

- Wraps the result of all module runs to provide easy access to results
  per server.
  [href]

- Default to transport 'localhost' if 'localhost' or '127.0.0.1' is used
  exclusively on the API object.
  [href]

0.3 (2014-05-28)
~~~~~~~~~~~~~~~~

- Adds a stern warning so users won't confuse this with the official Ansible API.
  [href]

0.2 (2014-05-21)
~~~~~~~~~~~~~~~~

- Change license to GPL v3 as required by Ansible.
  [href]

0.1 (2014-05-21)
~~~~~~~~~~~~~~~~

- Initial release.
  [href]
