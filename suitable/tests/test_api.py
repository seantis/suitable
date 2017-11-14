import os
import os.path
import pytest

from suitable.api import list_ansible_modules, Api
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


def test_results_single_server():
    result = Api('localhost').command('whoami')
    assert result.rc() == 0


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


def test_servers_list():
    host = Api(('localhost', ))
    assert host.command('whoami').rc('localhost') == 0


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


def test_unreachable():
    host = Api('255.255.255.255')

    assert '255.255.255.255' in host.servers

    try:
        host.command('whoami')
    except UnreachableError as e:
        assert '255.255.255.255' in str(e)
    else:
        assert False, "an error should have been thrown"

    assert '255.255.255.255' not in host.servers


def test_ignore_unreachable():
    host = Api('255.255.255.255', ignore_unreachable=True)

    assert '255.255.255.255' in host.servers
    host.command('whoami')
    assert '255.255.255.255' in host.servers


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
