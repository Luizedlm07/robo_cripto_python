
class Trade():

    def __init__(self):
        pass
    
    @classmethod
    def comprar(self, moeda, quantidade, objeto_moeda):
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

        info = client.get_symbol_info(moeda)

        price_filter = float(info['filters'][0]['tickSize'])
        price = objeto_moeda.cotacao * 1.002
        price = D.from_float(price).quantize(D(str(price_filter)))
        minimum = float(info['filters'][1]['minQty'])
        quant = D.from_float(quantidade).quantize(D(str(minimum)))

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

            order = client.get_all_orders(symbol=moeda, limit=1)
            print("Ordem: \n", order)

            if 'FILLED' in order[0]["status"]:
                print("Trade concluído!\n")
                _ = False
            else:
                time.sleep(10)

    
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

        info = client.get_symbol_info(moeda)

        price_filter = float(info['filters'][0]['tickSize'])
        price = objeto_moeda.cotacao * 0.997
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

            order = client.get_all_orders(symbol=moeda, limit=1)
            print("Ordem: \n", order)

            if cotacao > price:
                order = self.cancel_order(moeda, order[0]["orderId"])
            if 'FILLED' in order[0]["status"]:
                print("Trade concluído!\n")
                _ = False
            else:
                time.sleep(10)

        return order

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
    
'''
Média Móvel BNBETH | Menor = 0.17970800 | Maior = 0.17967778
Média Móvel SOLBNB | Menor = 0.06434000 | Maior = 0.06424646
Média Móvel ADABNB | Menor = 0.00112992 | Maior = 0.00112670
Média Móvel SOLETH | Menor = 0.01156280 | Maior = 0.01154586
Média Móvel ADAETH | Menor = 0.00020315 | Maior = 0.00020247
Gatilho de venda para BNBETH
Preço e quantidade:  0.1791 0.012
Traceback (most recent call last):
  File "/home/luiz/Documents/robo_cripto_python/main.py", line 51, in <module>
    mercado_bnbeth = Situacao_Mercado(bnbETH)
  File "/home/luiz/Documents/robo_cripto_python/situacao_mercado.py", line 4, in __init__
    self.gatilho_trade(objeto_moeda)
  File "/home/luiz/Documents/robo_cripto_python/situacao_mercado.py", line 7, in gatilho_trade
    from main import usuario
  File "/home/luiz/Documents/robo_cripto_python/main.py", line 51, in <module>
    mercado_bnbeth = Situacao_Mercado(bnbETH)
  File "/home/luiz/Documents/robo_cripto_python/situacao_mercado.py", line 4, in __init__
    self.gatilho_trade(objeto_moeda)
  File "/home/luiz/Documents/robo_cripto_python/situacao_mercado.py", line 19, in gatilho_trade
    order = usuario.verificar_gatilhos(objeto_moeda.symbol, 'SELL', objeto_moeda)      
  File "/home/luiz/Documents/robo_cripto_python/class_usuario.py", line 83, in verificar_gatilhos
    return Trade.vender(moeda, self.saldo, objeto_moeda)
  File "/home/luiz/Documents/robo_cripto_python/trade.py", line 84, in vender
    client.create_order(
  File "/home/luiz/.local/lib/python3.10/site-packages/binance/client.py", line 1397, in create_order
    return self._post('order', True, data=params)
  File "/home/luiz/.local/lib/python3.10/site-packages/binance/client.py", line 374, in _post
    return self._request_api('post', path, signed, version, **kwargs)
  File "/home/luiz/.local/lib/python3.10/site-packages/binance/client.py", line 334, in _request_api
    return self._request(method, uri, signed, **kwargs)
  File "/home/luiz/.local/lib/python3.10/site-packages/binance/client.py", line 315, in _request
    return self._handle_response(self.response)
  File "/home/luiz/.local/lib/python3.10/site-packages/binance/client.py", line 324, in _handle_response
    raise BinanceAPIException(response, response.status_code, response.text)
binance.exceptions.BinanceAPIException: APIError(code=-1013): Filter failure: MIN_NOTIONAL
'''