import gc
import os
import os.path
import pytest

from ansible.utils.display import Display
from crypt import crypt
from suitable.api import list_ansible_modules, Api
from suitable.mitogen import Api as MitogenApi
from suitable.mitogen import is_mitogen_supported
from suitable.errors import UnreachableError, ModuleError
from suitable.runner_results import RunnerResults
from suitable.compat import text_type


def test_auto_localhost():
    host = Api('localhost')
    assert host.options.connection == 'local'

    host = Api('localhost', connection='smart')
    assert host.options.connection == 'smart'


def test_sudo():
    host = Api('localhost', sudo=True)
    try:
        assert host.command('whoami').stdout() == 'root'
    except ModuleError as e:
        assert 'password' in e.result['module_stderr']


def test_module_args():
    upgrade = (
        'apt-get upgrade -y -o Dpkg::Options::="--force-confdef" '
        '-o Dpkg::Options::="--force-confold"'
    )

    try:
        Api('localhost').command(upgrade)
    except ModuleError as e:
        assert e.result['invocation']['module_args']['_raw_params'] == upgrade


def test_results():
    result = Api('localhost').command('whoami')
    assert result.rc('localhost') == 0
    assert result.stdout('localhost') is not None
    assert result['contacted']['localhost']['rc'] == 0

    with pytest.raises(AttributeError):
        result.asdf('localhost')

    result['contacted'] = []

    with pytest.raises(KeyError):
        result.rc('localhost')


@pytest.mark.parametrize("server", ('localhost', 'localhost:22'))
def test_results_single_server(server):
    result = Api(server).command('whoami')
    assert result.rc() == 0
    assert result.rc(server) == 0


def test_results_multiple_servers():
    result = RunnerResults({
        'contacted': {
            'web.seantis.dev': {'rc': 0},
            'db.seantis.dev': {'rc': 1}
        }
    })

    with pytest.raises(KeyError):
        result.rc()

    assert result.rc('web.seantis.dev') == 0
    assert result.rc('db.seantis.dev') == 1


@pytest.mark.parametrize("server", ('localhost', 'localhost:22'))
def test_servers_list(server):
    host = Api((server, ))
    assert host.command('whoami').rc(server) == 0


def test_valid_return_codes():
    host = Api('localhost')
    assert host._valid_return_codes == (0, )

    with host.valid_return_codes(0, 1):
        assert host._valid_return_codes == (0, 1)
        host.shell('whoami | grep -q asdfasdfasdf')

    assert host._valid_return_codes == (0, )


def test_list_ansible_modules():
    modules = list_ansible_modules()

    # look for some basic modules
    assert 'command' in modules
    assert 'file' in modules
    assert 'user' in modules
    assert 'shell' in modules
    assert 'git' in modules
    assert 'setup' in modules


def test_module_error():
    with pytest.raises(ModuleError):
        # command cannot include pipes
        Api('localhost').command('whoami | less')


@pytest.mark.parametrize("server", ('255.255.255.255', '255.255.255.255:22'))
def test_unreachable(server):
    host = Api(server)

    assert server in host.servers

    try:
        host.command('whoami')
    except UnreachableError as e:
        assert server in str(e)
    else:
        assert False, "an error should have been thrown"

    assert server not in host.servers


@pytest.mark.parametrize("server", ('localhost', 'localhost:22'))
def test_ignore_unreachable(server):
    host = Api(server, ignore_unreachable=True)

    assert server in host.servers
    host.command('whoami')
    assert server in host.servers


def test_custom_unreachable():
    class MyApi(Api):
        unreachable = []

        def on_unreachable_host(self, module, host):
            self.unreachable.append(host)
            return 'keep-trying'

    host = MyApi('255.255.255.255')

    host.command('whoami')
    assert len(host.unreachable) == 1

    host.command('whoami')
    assert len(host.unreachable) == 2

    host.command('whoami')
    assert len(host.unreachable) == 3


def test_custom_unreachable_default():
    class MyApi(Api):
        unreachable = []

        def on_unreachable_host(self, module, host):
            self.unreachable.append(host)

    host = MyApi('255.255.255.255')

    host.command('whoami')
    assert len(host.unreachable) == 1

    host.command('whoami')
    assert len(host.unreachable) == 1

    host.command('whoami')
    assert len(host.unreachable) == 1


def test_ignore_errors():
    host = Api('localhost', ignore_errors=True)
    result = host.command('whoami | less')

    assert result.rc() == 1
    assert result.cmd() == ['whoami', '|', 'less']


def test_error_string():
    try:
        Api('localhost').command('whoami | less')
    except ModuleError as e:
        # we don't have a msg so we mock that out, for coverage!
        e.result['msg'] = '0xdeadbeef'
        error_string = text_type(e)

        # we don't make many guarantees with the string messages, so
        # a basic somke test suffices here. This is not something to
        # depend on.

        assert '0xdeadbeef' in error_string
        assert 'command: whoami | less' in error_string
        assert 'Returncode: 1' in error_string
    else:
        assert False, "this needs to trigger an exception"


def test_escaping(tempdir):
    special_dir = os.path.join(tempdir, 'special dir with "-char')
    os.mkdir(special_dir)

    api = Api('localhost')
    api.file(
        dest=os.path.join(special_dir, 'foo.txt'),
        state='touch'
    )


def test_extra_vars(tempdir):
    api = Api('localhost', extra_vars={'path': tempdir})
    api.file(dest="{{ path }}/foo.txt", state='touch')

    assert os.path.exists(tempdir + '/foo.txt')


def test_environment():
    api = Api('localhost', environment={'FOO': 'BAR'})
    assert api.shell('echo $FOO').stdout() == 'BAR'

    api.environment['FOO'] = 'BAZ'
    assert api.shell('echo $FOO').stdout() == 'BAZ'


def test_server_with_port():
    # ideally we would test ipv6 here as well, but that doesn't work
    # on travis at the moment:
    # see https://github.com/travis-ci/travis-ci/issues/8891
    for definition in ('localhost:22', ['localhost:22']):
        api = Api(definition)

        assert api.servers == ['localhost:22']

        hosts, ports = zip(tuple(*api.hosts_with_ports))
        assert hosts == ('localhost', )
        assert ports == (22, )

        result = Api('localhost').command('whoami')
        assert result.rc() == 0


def test_same_server_multiple_ports():
    api = Api(('localhost', 'localhost:22'))
    assert len(api.servers) == 2

    # Ansible groups these calls, so we only get one result back
    result = api.command('whoami')
    assert len(result['contacted']) == 1


def test_single_display_module():
    assert sum(1 for obj in gc.get_objects() if isinstance(obj, Display)) == 1


@pytest.mark.skipif(not is_mitogen_supported(), reason="incompatible mitogen")
def test_mitogen_integration():
    try:
        result = MitogenApi('localhost').command('whoami')
        assert len(result['contacted']) == 1
    except SystemExit:
        pass


def test_list_args():
    api = Api('localhost')

    # api.assert is not valid Python syntax
    getattr(api, 'assert')(that=[
        "'bar' != 'foo'",
        "'bar' == 'bar'"
    ])


def test_dict_args(tempdir):
    api = Api('localhost')
    api.set_stats(data={'foo': 'bar'})


def test_disable_hostkey_checking(api):
    api.host_key_checking = False
    assert api.command('whoami').stdout() == 'root'


def test_enable_hostkey_checking_vanilla(container):
    # if we do not use 'paramiko' here, we get the following error:
    # > Using a SSH password instead of a key is not possible because Host Key
    # > checking is enabled and sshpass does not support this.
    # > Please add this host's fingerprint to your known_hosts file to
    # > manage this host.
    api = container.vanilla_api(connection='paramiko')

    with pytest.raises(UnreachableError):
        assert api.command('whoami').stdout() == 'root'


def test_interleaving(container):
    # make sure we can interleave calls of different API objects
    password = crypt("foobar", "salt")

    root = container.vanilla_api(connection='paramiko')
    root.host_key_checking = False

    root.command('useradd --non-unique --uid 0 foo -p ' + password)
    root.command('useradd --non-unique --uid 0 bar -p ' + password)

    foo = container.vanilla_api(
        connection='paramiko', remote_user='foo', remote_pass='foobar')
    bar = container.vanilla_api(
        connection='paramiko', remote_user='bar', remote_pass='foobar')

    foo.host_key_checking = False
    bar.host_key_checking = False

    assert foo.command('id -g').stdout() == '1000'
    assert bar.command('id -g').stdout() == '1001'

    assert foo.command('id -g').stdout() == '1000'
    assert bar.command('id -g').stdout() == '1001'
