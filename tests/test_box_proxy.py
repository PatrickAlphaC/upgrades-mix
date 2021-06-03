import pytest
from brownie import (
    Box,
    TransparentUpgradeableProxy,
    ProxyAdmin,
    Contract,
    network,
    config,
)
from scripts.helpful_scripts import get_account, encode_function_data


def test_proxy_delegates_calls():
    account = get_account()
    box = Box.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()]["verify"],
    )
    proxy_admin = ProxyAdmin.deploy(
        {"from": account},
    )
    box_encoded_initializer_function = encode_function_data()
    proxy = TransparentUpgradeableProxy.deploy(
        box.address,
        proxy_admin.address,
        box_encoded_initializer_function,
        {"from": account, "gas_limit": 1000000},
    )
    proxy_box = Contract.from_abi("Box", proxy.address, Box.abi)
    assert proxy_box.retrieve() == 0
    proxy_box.store(1, {"from": account})
    assert proxy_box.retrieve() == 1
    with pytest.raises(AttributeError):
        proxy_box.increment({"from": account})
