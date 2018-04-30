def to_host_and_port(server):
    # [ipv6]:port
    if server.startswith('['):
        host, port = server.rsplit(':', 1)
        host = host.strip('[]')

    # host:port
    elif server.count(':') == 1:
        host, port = server.split(':', 1)

    # host
    else:
        host, port = server, None

    return host, port and int(port) or None


def to_server(host, port):
    if port is None:
        return host

    if ':' in host:
        form = '[{host}]:{port}'
    else:
        form = '{host}:{port}'

    return form.format(host=host, port=port)
