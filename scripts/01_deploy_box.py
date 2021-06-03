#!/usr/bin/python3
from brownie import (
    Box,
    TransparentUpgradeableProxy,
    ProxyAdmin,
    config,
    network,
)
from scripts.helpful_scripts import get_account, encode_function_data


def main():
    account = get_account()
    print(f"Deploying to {network.show_active()}")
    box = Box.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    # Optional, deploy the ProxyAdmin and use that as the admin contract
    proxy_admin = ProxyAdmin.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )

    # If we want an intializer function we can add
    # `initializer=box.store, 1`
    # to simulate the initializer being the `store` function
    # with a `newValue` of 1
    box_encoded_initializer_function = encode_function_data()
    # box_encoded_initializer_function = encode_function_data(initializer=box.store, 1)
    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        # account.address,
        proxy_admin.address,
        box_encoded_initializer_function,
        {"from": account, "gas_limit": 1000000},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    print(f"Proxy deployed to {proxy} ! You can now upgrade it to BoxV2!")
    # function_call = encode_function_data(initializer=box.retrieve)
    # print(proxy.call(function_call))
