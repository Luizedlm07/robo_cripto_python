from main import client, Client
import requests

class Par_moeda():          ## Classe que armazena todos os dados referentes a moedas

    def __init__(self, symbol):
        self.symbol = symbol
        self.cotacao = self.cotar(symbol)
        self.mm_menor = self.calc_mm(symbol)
        self.mm_maior = self.calc_mm(symbol)
        self.lista_mm_menor = []
        self.lista_mm_maior = []


    def cotar(self,symbol):
        ultima_transacao = client.get_recent_trades(symbol=symbol, limit=1)
        return float(ultima_transacao[-1]['price'])

    def calc_mm_menor(self, symbol):
        for kline in client.get_historical_klines_generator(symbol, Client.KLINE_INTERVAL_1MINUTE, limit=14):
            ma14 += float(kline[4])
        return ma14 / 14

    def calc_mm_maior(self,symbol):
        for kline in client.get_historical_klines_generator(symbol, Client.KLINE_INTERVAL_1MINUTE, limit=36):
            ma36 += float(kline[4])
        return ma36 / 36
    
    def armazenar_medias_moveis(self):
        self.lista_mm_menor.append(self.mm_menor)
        self.lista_mm_menor.append(self.mm_maior)



        
class Usuario():                ## Classe que armazena dados referentes ao usuário

    def __init__(self):
        self.moeda, self.saldo = self.verificar_moeda_atual()
        self.negociaveis = self.verificar_negociaveis()
        self.trades = self.consultar_trade()
        self.orders = self.consultar_order()

    def verificar_moeda_atual(self):


        def converter(moeda):

            symbol = moeda + 'USDT'
            url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
            response = requests.get(url)

            if response.status_code == 200:
                price = response.json()['price']
                saldo_convertido = float(ativo["free"]) * price
                print(f'O preço atual de {symbol} é de {price} dólares.')
                return moeda, saldo_convertido

            else:
                print(f'Erro ao obter o preço de {symbol}')


        info = client.get_account()

        lista_ativo = info["balances"]
        moeda = []
        saldo = []

        for ativo in lista_ativo:
            if float(ativo["free"]) > 0:
                moeda.append(ativo["asset"])
                saldo.append(converter(ativo["asset"]))
            maior_valor = max(saldo)
            indice_maior_valor = saldo.index(maior_valor)

        return moeda[indice_maior_valor], saldo[indice_maior_valor]
    


    def consultar_trade(self):
        pass

    def consultar_order(self):
        ordem = client.get_all_orders(symbol=self.moeda, limit=1)
        return ordem
        


class Situacao_Mercado():

    def __init__(self):
        self.pares = ['BNBETH','SOLBNB','ADABNB','ADAETH','SOLETH']
        self.negociaveis = []

    def verificar_negociaveis(self, moeda):

        for par in self.pares:

            if moeda in par:
                self.negociaveis.append(par)


    def gatilho_trade(self, mm_menor, mm_maior, moeda_atual, symbol, saldo):        ## Se a minha moeda atual for igual a primeira moeda do par, ela pode vender. Se for igual a segunda moeda, pode comprar

        for par in self.negociaveis:
            if moeda_atual == par[0:2]:
                if mm_menor[-1] < mm_maior[-1] and mm_menor[-2] > mm_maior[-2]:
                        order = Trade.vender(par, saldo)
                        return order
                
            if moeda_atual == par[-1:-3]:
                if symbol[-1:-3] in par:
                        if mm_menor[-1] > mm_maior[-1] and mm_menor[-2] < mm_maior[-2]:
                            order = Trade.comprar(par, saldo)
                            return order


class Trade():

    def __init__(self):
        pass
    
    def comprar(self, moeda, saldo):
        from main import client
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
    
    def vender(self, moeda, saldo, cotacao):

        
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
        price = cotacao * 0.995
        price = D.from_float(price).quantize(D(str(price_filter)))
        minimum = float(info['filters'][1]['minQty'])
        quant = D.from_float(saldo).quantize(D(str(minimum)))

        print("Preço e quantidade: ", price, quant)
        print(f"{price * D('0.995')}")

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
            print(Par_moeda.cotar(moeda))

            ordem = client.get_all_orders(symbol=moeda, limit=1)
            print("Ordem: \n", ordem)

            if Par_moeda.cotar(moeda) > cotacao:
                self.cancel_order()
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
    