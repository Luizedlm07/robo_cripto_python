from main import saldoETH, saldoBNB, client
from binance.enums import *
from binance.client import Client
from binance import exceptions

def comprar(moeda, moeda_atual):
    from variaveis import diminuir_valor
    _ = 0
    if moeda_atual == 'BNB':
        while _ == 0:
            diminuir_valor -= 0.001
            try: 
                order = client.create_order(
                symbol=moeda,
                side=SIDE_BUY,
                type=ORDER_TYPE_MARKET,
                quoteOrderQty=f'{float(saldoBNB * diminuir_valor):.8f}'
                )
                _ = 1
            except exceptions.BinanceAPIException:
                print("Tentando comprar...")
                continue

    if moeda_atual == 'ETH':
        while _ == 0:
            diminuir_valor -= 0.001
            try: 
                order = client.create_order(
                symbol=moeda,
                side=SIDE_BUY,
                type=ORDER_TYPE_MARKET,
                quoteOrderQty=f'{float(saldoETH * diminuir_valor):.8f}'
                )
                _ = 1
            except exceptions.BinanceAPIException:
                print("Tentando comprar...")
                cont += 1
                if cont <= 20:
                    continue
                else:
                    order = client.create_order(
                    symbol=moeda,
                    side=SIDE_BUY,
                    type=ORDER_TYPE_MARKET,
                    quoteOrderQty=f'{float(saldoETH * diminuir_valor):.8f}'
                    )


    return order


def vender(moeda, saldo):
    from variaveis import diminuir_valor
    cont = 0
    _ = 0
    while _ == 0:
        diminuir_valor -= 0.003
        try:
            order = client.create_order(
            symbol=moeda,
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quoteOrderQty=f'{float(1 * diminuir_valor):.8f}'
            )
            _ = 1
        except exceptions.BinanceAPIException:
            print("Tentando vender...")
            cont += 1
            # if cont <= 30:
            #     continue
            # else: 
            #     order = client.create_order(
            #     symbol=moeda,
            #     side=SIDE_SELL,
            #     type=ORDER_TYPE_MARKET,
            #     quantity=f'{float(saldo * diminuir_valor):.8f}'
            #     )

    return order
