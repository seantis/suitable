import paramiko
import port_for
import pytest
import shutil
import subprocess
import tempfile
import time

from uuid import uuid4
from suitable import Api
from suitable.mitogen import Api as MitogenApi
from suitable.mitogen import is_mitogen_supported


if is_mitogen_supported():
    APIS = ('vanilla', 'mitogen')
else:
    APIS = ('vanilla', )


class Container(object):

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def spawn_api(self, api_class, **kwargs):
        options = {
            'remote_user': self.username,
            'remote_pass': self.password,
            'connection': 'smart',
            'extra_vars': {
                'ansible_python_interpreter': '/usr/bin/python3'
            }
        }

        options.update(kwargs)

        return api_class(
            f'{self.host}:{self.port}',
            ** options
        )

    def vanilla_api(self, **kwargs):
        return self.spawn_api(Api, **kwargs)

    def mitogen_api(self, **kwargs):
        return self.spawn_api(MitogenApi, **kwargs)


@pytest.fixture(scope="function")
def tempdir():
    tempdir = tempfile.mkdtemp()
    yield tempdir
    shutil.rmtree(tempdir)


def wait_for_sshd(host, port):
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    timeout = 5
    started = time.monotonic()
    while time.monotonic() - started < timeout:
        try:
            client.connect(
                host,
                port,
                allow_agent=False,
                look_for_keys=False
            )
        except paramiko.ssh_exception.SSHException as e:
            # socket is open, but no SSH service responded
            if not e.args[0].startswith('Error reading SSH protocol banner'):
                return
        except paramiko.ssh_exception.NoValidConnectionsError:
            pass

        finally:
            client.close()

        time.sleep(.5)

    raise RuntimeError('Failed to initalize sshd in docker container')


@pytest.fixture(scope="function")
def container():
    port = port_for.select_random()
    name = f'suitable-container-{uuid4().hex}'

    subprocess.check_call((
        'docker', 'run', '-d', '--rm', '-it',
        '--name', name,
        '-p', f'127.0.0.1:{port}:22/tcp',
        'takeyamajp/ubuntu-sshd:ubuntu22.04'
    ))
    wait_for_sshd('127.0.0.1', port)

    yield Container('127.0.0.1', port, 'root', 'root')

    subprocess.call(('docker', 'stop', name))


@pytest.fixture(scope="function", params=APIS)
def api(request, container):
    yield getattr(container, f'{request.param}_api')(connection='paramiko')
