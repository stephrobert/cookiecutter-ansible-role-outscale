"""Role testing files using testinfra."""

import os
import pytest

@pytest.fixture()
def AnsibleVars(host):
    return host.ansible("include_vars", os.path.join("./defaults/", "main.yml"))["ansible_facts"]

def test_installed_packages(host):
    # Le pacakge zabiix-agent est installé et la version est celle attendue
    unattended_upgrades = host.package("unattended-upgrades")
    assert unattended_upgrades.is_installed
