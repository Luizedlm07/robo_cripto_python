from main import saldoETH, saldoBNB, client
from binance.enums import *
from binance.client import Client
from binance import exceptions


diminuir_valor = 0.999

def comprar(moeda):
    _ = 0
    while _ == 0:
        diminuir_valor -= 0.001
        try: 
            order = client.create_test_order(
                symbol=moeda,
                side=SIDE_BUY,
                type=ORDER_TYPE_MARKET,
                quoteOrderQty=f'{float(saldoETH * diminuir_valor):.8f}'
                )
            _ = 1
        except exceptions.BinanceAPIException:
            print("Tentando comprar...")
            continue
    return order

diminuir_valor = 0.999

def vender(moeda):
    _ = 0
    while _ == 0:
        diminuir_valor -= 0.001
        try:
            order = client.create_order(
            symbol=moeda,
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quantity=f'{float(saldoBNB * diminuir_valor):.8f}'
            )
            _ = 1
        except exceptions.BinanceAPIException:
            print("Tentando vender...")
            continue
    return order
