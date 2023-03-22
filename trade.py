from class_usuario import Usuario


class Trade():

    def __init__(self):
        pass
    
    @classmethod
    def comprar(self, moeda, saldo):
        from class_usuario import client
        from binance import exceptions
        from binance.enums import (
                ORDER_TYPE_LIMIT,
                ORDER_TYPE_MARKET,
                SIDE_BUY,
                SIDE_SELL,
                TIME_IN_FORCE_GTC,
                TIME_IN_FORCE_IOC
            )

    
        diminuir_valor = 0.990
        _ = 0

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
                    quoteOrderQty=f'{float(saldo * diminuir_valor):.4f}'
                    )

        return order
    
    @classmethod
    def vender(self, moeda, saldo, objeto_moeda):

        from class_usuario import client
        from decimal import Decimal as D
        import time
        from binance.enums import (
            ORDER_TYPE_LIMIT,
            ORDER_TYPE_MARKET,
            SIDE_BUY,
            SIDE_SELL,
            TIME_IN_FORCE_GTC,
            TIME_IN_FORCE_IOC
        )

        info = Usuario.client.get_symbol_info(moeda)

        price_filter = float(info['filters'][0]['tickSize'])
        price = cotacao * 0.995
        price = D.from_float(price).quantize(D(str(price_filter)))
        minimum = float(info['filters'][1]['minQty'])
        quant = D.from_float(saldo).quantize(D(str(minimum)))

        print("Preço e quantidade: ", price, quant)

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
            cotacao = objeto_moeda.cotar(moeda)
            print()

            ordem = Usuario.client.get_all_orders(symbol=moeda, limit=1)
            print("Ordem: \n", ordem)

            if cotacao > price:
                self.cancel_order(moeda, ordem[0]["orderId"])
            if 'FILLED' in ordem[0]["status"]:
                print("Trade concluído!\n")
                _ = False
            else:
                time.sleep(10)

        return ordem

    def cancel_order(self, symbol, order_id):

        import requests
        import json
        import hashlib
        import hmac
        import time
        from secrets_1 import api_key, api_secret

        endpoint = 'https://api.binance.com/api/v3/order'

        
        params = {
            'symbol': symbol,
            'orderId': order_id,
            'timestamp': int(time.time() * 1000)
        }


        query_string = '&'.join([f"{key}={params[key]}" for key in params])
        signature = hmac.new(api_secret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256).hexdigest()
        params['signature'] = signature

        
        response = requests.delete(endpoint, headers={'X-MBX-APIKEY': api_key}, params=params)

        
        return json.loads(response.text)
    