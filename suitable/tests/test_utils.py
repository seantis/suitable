from suitable.utils import to_host_and_port, to_server


def test_to_host_and_port():
    assert to_host_and_port('[::1]:22') == ('::1', 22)
    assert to_host_and_port('::1') == ('::1', None)

    assert to_host_and_port('localhost') == ('localhost', None)
    assert to_host_and_port('localhost:22') == ('localhost', 22)


def test_to_server():
    assert to_server('::1', None) == '::1'
    assert to_server('::1', 22) == '[::1]:22'

    assert to_server('localhost', None) == 'localhost'
    assert to_server('localhost', 22) == 'localhost:22'
