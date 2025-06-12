from __future__ import annotations

import pytest

from suitable.inventory import Inventory
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from suitable.types import Hosts


def test_single_host() -> None:
    host = 'example.org:22'
    inventory = Inventory(hosts=host)
    assert inventory[host]['ansible_host'] == 'example.org'
    assert inventory[host]['ansible_port'] == 22


@pytest.mark.parametrize('hosts', ('example.org:22 example.org',
                                   ['example.org:22', 'example.org'],
                                   ('example.org:22', 'example.org')))
def test_host_sequence(hosts: Hosts) -> None:
    inventory = Inventory(hosts=hosts)
    assert 'example.org' in inventory
    assert 'example.org:22' in inventory


def test_host_dict() -> None:
    hosts = {'example.org': {'key1': 'var1'}, 'host.example.org': {}}
    inventory = Inventory(hosts=hosts)
    assert 'host.example.org' in inventory
    assert inventory['example.org']['key1'] == 'var1'
