#!/usr/bin/python3
from brownie import (
    BoxV2,
    TransparentUpgradeableProxy,
    ProxyAdmin,
    config,
    network,
)
from scripts.helpful_scripts import get_account, upgrade


def main():
    account = get_account()
    print(f"Deploying to {network.show_active()}")
    box_v2 = BoxV2.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    proxy = TransparentUpgradeableProxy[len(TransparentUpgradeableProxy) - 1]
    proxy_admin = ProxyAdmin[len(ProxyAdmin) - 1]
    upgrade(account, proxy, box_v2, proxy_admin_contract=proxy_admin)
    print("Proxy has been upgraded!")
    print(proxy.retrieve())
    proxy.increment({"from": account})
    print(proxy.retrieve())
