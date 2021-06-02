#!/usr/bin/python3
from brownie import Box, TransparentUpgradeableProxy, accounts, config, network
from scripts.helpful_scripts import get_account


def main():
    account = get_account()
    print(f"Deploying to {network.show_active()}")
    box = Box.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # Optional, deploy the ProxyAdmin and use that as the admin contract
    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        account.address,
        "0x",
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"Proxy deployed to {proxy}! You can now upgrade it to BoxV2!")
