#!/usr/bin/python3

import pytest

def test_add_liquidity_ETH(DAI, WETH, accounts, SwapRouter, CellarPoolShareContract):
    SwapRouter.exactOutputSingle([WETH, DAI, 500, accounts[0], 2 ** 256 - 1, 3000 * 10 ** 18, 10 * 10 ** 18, 0], {"from": accounts[0], "value": 10 * 10 ** 18})
    SwapRouter.exactOutputSingle([WETH, DAI, 500, accounts[1], 2 ** 256 - 1, 3000 * 10 ** 18, 10 * 10 ** 18, 0], {"from": accounts[1], "value": 10 * 10 ** 18})
    DAI.approve(CellarPoolShareContract, 3000 * 10 ** 18, {"from": accounts[0]})
    DAI.approve(CellarPoolShareContract, 3000 * 10 ** 18, {"from": accounts[1]})
    ETH_amount = 10 ** 18
    DAI_amount = 1000 * 10 ** 18
    cellarAddParams = [DAI_amount, ETH_amount, 0, 0, 2 ** 256 - 1]
    CellarPoolShareContract.addLiquidityForUniV3(cellarAddParams, {"from": accounts[0], "value": 1 * 10 ** 18})
    CellarPoolShareContract.addLiquidityForUniV3(cellarAddParams, {"from": accounts[0], "value": 1 * 10 ** 18})
    CellarPoolShareContract.addLiquidityForUniV3(cellarAddParams, {"from": accounts[0], "value": 1 * 10 ** 18})
    cellarAddParams = [DAI_amount, ETH_amount, 0, 0, 2 ** 256 - 1]
    CellarPoolShareContract.addLiquidityForUniV3(cellarAddParams, {"from": accounts[1], "value": 1 * 10 ** 18})
    CellarPoolShareContract.addLiquidityForUniV3(cellarAddParams, {"from": accounts[1], "value": 1 * 10 ** 18})
    CellarPoolShareContract.addLiquidityForUniV3(cellarAddParams, {"from": accounts[1], "value": 1 * 10 ** 18})
    assert CellarPoolShareContract.balanceOf(accounts[0]) == CellarPoolShareContract.balanceOf(accounts[1])

def test_remove_liquidity(DAI, WETH, accounts, CellarPoolShareContract):
    bal = CellarPoolShareContract.balanceOf(accounts[1])
    cellarRemoveParams = [bal // 3, 0, 0, 2 ** 256 - 1]
    CellarPoolShareContract.removeLiquidityFromUniV3(cellarRemoveParams, {"from": accounts[1]})
    assert bal - CellarPoolShareContract.balanceOf(accounts[1]) == bal // 3

def test_remove_liquidity_ETH(DAI, WETH, accounts, CellarPoolShareContract):
    bal = CellarPoolShareContract.balanceOf(accounts[1])
    cellarRemoveParams = [bal // 2, 0, 0, 2 ** 256 - 1]
    CellarPoolShareContract.removeLiquidityFromUniV3(cellarRemoveParams, {"from": accounts[1]})
    assert bal - CellarPoolShareContract.balanceOf(accounts[1]) == bal // 2