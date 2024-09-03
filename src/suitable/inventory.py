from __future__ import annotations

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from suitable.types import Hosts, HostVariables, Incomplete
    from typing import Dict

    _Base = Dict[str, HostVariables]
else:
    _Base = dict


class Inventory(_Base):

    def __init__(
        self,
        ansible_connection: Incomplete | None = None,
        hosts: Hosts | None = None
    ) -> None:
        super().__init__()
        self.ansible_connection = ansible_connection
        if hosts:
            self.add_hosts(hosts)

    def add_host(self, server: str, host_variables: HostVariables) -> None:
        self[server] = {}

        # [ipv6]:port
        if server.startswith('['):
            host, port_str = server.rsplit(':', 1)
            self[server]['ansible_host'] = host = host.strip('[]')
            self[server]['ansible_port'] = int(port_str)

        # host:port
        elif server.count(':') == 1:
            host, port_str = server.split(':', 1)
            self[server]['ansible_host'] = host
            self[server]['ansible_port'] = int(port_str)

        # Add vars
        self[server].update(host_variables)

        # Localhost
        if not self.ansible_connection:
            # Get hostname (either ansible_host or server)
            host = self[server].get('ansible_host', server)
            port = self[server].get('ansible_port', 22)
            if host in ('localhost', '127.0.0.1', '::1') and port == 22:
                self[server]['ansible_connection'] = 'local'

    def add_hosts(self, servers: Hosts) -> None:
        if isinstance(servers, str):
            for server in servers.split():
                self.add_host(server, {})
        elif isinstance(servers, dict):
            for server, host_variables in servers.items():
                self.add_host(server, host_variables)
        else:
            for server in servers:
                self.add_host(server, {})
