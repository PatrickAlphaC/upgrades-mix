# #!/usr/bin/python3
# from brownie import (
#     Box,
#     TransparentUpgradeableProxy,
#     ProxyAdmin,
#     config,
#     network,
# )
# from scripts.helpful_scripts import get_account, encode_function_data


# def main():
#     account = get_account()
#     print(f"Deploying to {network.show_active()}")
#     box = Box[len(Box) - 1]
#     proxy = TransparentUpgradeableProxy[len(TransparentUpgradeableProxy) - 1]
#     # function_call = encode_function_data(initializer=box.retreive)
#     # print(proxy.call(function_call))
#     print(proxy.retrieve())
