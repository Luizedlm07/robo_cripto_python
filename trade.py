from main import saldoETH, saldoBNB, client
from binance.enums import *
from binance.client import Client
from binance import exceptions

def comprar(moeda, moeda_atual):
    diminuir_valor = 0.990
    _ = 0
    if moeda_atual == 'BNB':
        cont = 0
        while _ == 0:
            diminuir_valor -= 0.003
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
                cont += 1
                if cont <= 300:
                    continue
                else: 
                    order = client.create_order(
                    symbol=moeda,
                    side=SIDE_BUY,
                    type=ORDER_TYPE_MARKET,
                    quoteOrderQty=f'{float(saldoBNB * diminuir_valor):.8f}'
                    )

    if moeda_atual == 'ETH':
        cont = 0
        while _ == 0:
            diminuir_valor -= 0.003
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
                if cont <= 300:
                    continue
                else:
                    order = client.create_order(
                    symbol=moeda,
                    side=SIDE_BUY,
                    type=ORDER_TYPE_MARKET,
                    quoteOrderQty=f'{float(saldoETH * diminuir_valor):.8f}'
                    )

    return order


def vender(moeda, saldo, valor_atual):

    import time
    # diminuir_valor = 0.999
    # cont = 0
    # _ = 0
    # while _ == 0:
    # diminuir_valor -= 0.003
        # try:
    order = client.create_order(
    symbol=moeda,
    side=SIDE_SELL,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    price=f"{valor_atual * 1.0050:.6f}",
    quantity=saldo
    )
    _ = True
    while _:

        print('Ordem aberta...')
        ordem = client.get_all_orders(symbol=moeda, limit=1)
        print("Ordem: \n", ordem)

        if 'FILLED' in ordem["status"]:
            print("Trade concluído! Ordens canceladas. \n")
            _ = False
        else:
            time.sleep(10)

        # _ = 1
        # except exceptions.BinanceAPIException:
        #     print("Tentando vender...")
        #     cont += 1
        #     if cont <= 3000:
        #         continue
        #     else: 
        #         order = client.create_order(
        #         symbol=moeda,
        #         side=SIDE_SELL,
        #         type=ORDER_TYPE_MARKET,
        #         quoteOrderQty=f'{float(0.1 * diminuir_valor):.8f}'
        #         )

    return order

def vender_bnbETH():
    diminuir_valor = 0.990
    _ = True
    while _:
        try:    
            order = client.create_order(
            symbol='BNBETH',
            side=SIDE_SELL,
            type=ORDER_TYPE_MARKET,
            quoteOrderQty=f'{float(saldoBNB * diminuir_valor):.8f}'
            )
            _ = False
        except exceptions.BinanceAPIException:
            print("Tentando vender BNBETH...")
            continue
    return order
