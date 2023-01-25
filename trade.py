from main import saldoETH, saldoBNB, client
from binance.enums import *
from binance import exceptions

def comprar(moeda, moeda_atual, saldo):
    
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
                quoteOrderQty=f'{saldo * diminuir_valor:.4f}'
                )
                _ = 1

            except exceptions.BinanceAPIException:
                print("Tentando comprar...")
                cont += 1

                if cont <= 30:
                    continue

                else: 
                    order = client.create_order(
                    symbol=moeda,
                    side=SIDE_BUY,
                    type=ORDER_TYPE_MARKET,
                    quoteOrderQty=f'{float(saldoBNB * diminuir_valor):.4f}'
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
                quoteOrderQty=f'{float(saldoETH * diminuir_valor):.5f}'
                )
                _ = 1

            except exceptions.BinanceAPIException:
                print("Tentando comprar...")
                cont += 1

                if cont <= 30:
                    continue

                else:
                    order = client.create_order(
                    symbol=moeda,
                    side=SIDE_BUY,
                    type=ORDER_TYPE_MARKET,
                    quoteOrderQty=f'{float(saldoETH * diminuir_valor):.5f}'
                    )

    return order


def vender(moeda, saldo, valor_atual):
    
    from decimal import Decimal as D
    import time

    info = client.get_symbol_info(moeda)

    price_filter = float(info['filters'][0]['tickSize'])
    price = valor_atual * 1.005
    price = D.from_float(price).quantize(D(str(price_filter)))
    minimum = float(info['filters'][1]['minQty'])
    quant = D.from_float(saldo).quantize(D(str(minimum)))

    print("Preço e quantidade: ", price, quant)
    print(f"{price * D('1.005')}")

    client.create_order(
    symbol=moeda,
    side=SIDE_SELL,
    type=ORDER_TYPE_LIMIT,
    timeInForce=TIME_IN_FORCE_GTC,
    price=f"{price}",
    quantity=f"{quant}"
    )
    _ = True
    while _:

        print('Ordem aberta...')
        ordem = client.get_all_orders(symbol=moeda, limit=1)
        print("Ordem: \n", ordem)

        if 'FILLED' in ordem[0]["status"]:
            print("Trade concluído!\n")
            _ = False
        else:
            time.sleep(10)

    return ordem

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
