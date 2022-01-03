from brownie import CellarPoolShare, accounts

def main():
    acct = accounts.load("deployer_account")
    name = "Test Sommelier Dai-Eth Cellar"
    symbol = "TESTSOMMDAIETH"
    token0 = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
    token1 = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    cellarTickInfo = [[0,-82030,-83310,1]]
    CellarPoolShare.deploy(name, symbol, token0, token1, 3000, cellarTickInfo, {"from":acct})