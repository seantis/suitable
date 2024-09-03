Suitable
========

An Ansible API for humans.

Introduction
------------

Ansible is a configuration management tool written in Python. Even though it
is written in Python its configuration syntax is decidedly un-pythonic.

To write ansible configuration is to write YAML files. Suitable *does not*
try to change that. Suitable tries to be a simple Ansible API abstraction
in Python.

With Suitable you can write Python code that has easy access to the
plethora of modules that Ansible offers. As such it is great for
scripts that automate migrations, upgrades or other little tasks.

Suitable is not an alternative to Ansible, it is a tool to complement
it. Do not use Suitable to manage your server fleet. Use Suitable
to boss your servers around from time to time.

Warning
-------

Suitable is not endorsed by Ansible and it is not affilated with it. Use at
your own peril.

The official way to use Ansible from Python is documented here:
`<http://docs.ansible.com/ansible/developing_api.html>`_

Installation
------------

To install suitable, simply use pip. This will install Ansible 2.x
automatically as a dependency::

    pip install suitable

Examples
--------

Create the user 'denis' on 'web.seantis.dev' and 'db.seantis.dev'::

    from suitable import Api

    hosts = Api(['web.seantis.dev', 'db.seantis.dev'])
    hosts.user(name='denis')

Create the user 'postgres' on 'db.seantis.dev'::

    dbhost = Api('db.seantis.dev')
    dbhost.user(name='postgres')

List the mounts on 'backup.seantis.dev'::

    backuphost = Api('backup.seantis.dev')
    backuphost.setup(filter='ansible_mounts')

Connect to a server using a username and a password::

    from getpass import getpass

    username = 'admin'
    password = getpass()

    api = Api(
        'web.seantis.dev',
        remote_user=username,
        remote_pass=password
    )

    print(api.command('whoami').stdout())  # prints 'admin'

Run a command on multiple servers and get the output for each::

    servers = ['a.example.org', 'b.example.org']

    api = Api(servers)
    result = api.command('whoami')

    for server in servers:
        print(result.stdout(server))

Or alternatively::

    api = Api(['a.example.org', 'b.example.org'])
    results = api.command('whoami')

    for server, result in results['contacted'].items():
        if 'stdout' in result:
            print(server, result['stdout'])

The latter is more robust for optional result components, since not
every server's result may contain it.


Which Modules are Available?
----------------------------

All of them! Suitable is a wrapper around all Ansible modules. Here's a list
of all Ansible modules:

`<http://docs.ansible.com/ansible/modules_by_category.html>`_

Say you want to use the file module, which is documented here:

`<http://docs.ansible.com/ansible/file_module.html>`_

Take the first example of the file module::

    - file: path=/etc/foo.conf owner=foo group=foo mode=0644

It can be directly translated into the following Suitable call::

    api.file(path='etc/foo.conf', owner='foo', mode='0644')

This works for any Ansible module.

Mitogen Support
---------------

Suitable supports `<https://mitogen.readthedocs.io>`_ for major performance
gains. Note that this support is somewhat experimental and should be used
with caution.

To use mitogen with Suitable, install it first, alongside Suitable::

    pip install suitable
    pip install mitogen

Afterwards, change your import slightly to use an adapted Suitable Api class::

    from suitable.mitogen import Api

This class works exactly like the vanilla Suitable Api, the difference is that
it registers mitogen with Ansible automatically and switches the default
strategy to 'mitogen_linear'.

You can also use the alternative 'mitogen_free' strategy with this class::

    Api('example.org', strategy='mitogen_free')

API Documentation
-----------------

To learn more about Suitable's API have a look at the API documentation:

:doc:`api`.

If you have any questions do not hesitate to
`open an issue <https://github.com/seantis/suitable/issues>`_.

Source
------

`<https://github.com/seantis/suitable>`_

License
-------

Suitable is released under GPLv3 (compatible with Ansible).

Navigation
----------

.. toctree::
   :maxdepth: 2

   Overview <self>
   API Documentation <api>