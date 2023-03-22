from binance.client import Client
from secrets_1 import api_key, api_secret
import requests
client = Client(api_key, api_secret)

class Usuario():                ## Classe que armazena dados referentes ao usuário

    def __init__(self):
        self.moeda, self.saldo = self.verificar_moeda_atual()
        self.trades = self.consultar_trade()
        self.orders = self.consultar_order()
        self.client = client

    def verificar_moeda_atual(self):


        def converter(moeda):

            symbol = moeda + 'USDT'
            url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
            response = requests.get(url)

            if response.status_code == 200:
                price = response.json()['price']
                saldo_convertido = float(ativo["free"]) * float(price)
                print(f'O preço atual de {symbol} é de {float(price):.2f} dólares.')
                print(f'A conversão do seu saldo de {symbol} em dólares é {saldo_convertido:.2f}')
                return saldo_convertido

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
            if saldo[-1] is None:
                del saldo[-1]
        maior_valor = max(saldo)
        indice_maior_valor = saldo.index(maior_valor)

        return moeda[indice_maior_valor], saldo[indice_maior_valor]
    


    def consultar_trade(self):
        pass

    def consultar_order(self):
        pass
