Suitable
========

An Ansible API for humans.

Introduction
------------

Ansible is a configuration management tool written in Python. Even though it
is written in Python it's configuration syntax is decidedly un-pythonic.

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
        remote_pass=passord
    )

    print api.command('whoami').stdout()  # prints 'admin'

Run a command on multiple servers and get the output for each::

    servers = ['a.example.org', 'b.example.org']

    api = Api(servers)
    result = api.command('whoami')

    for server in servers:
        print result.stdout(server)

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

More Documentation
------------------

More documentation is coming.

For now have a look at Suitable's Api class to learn more:

:doc:`api`.

License
-------

Suitable is released under GPLv3 (compatible with Ansible).
