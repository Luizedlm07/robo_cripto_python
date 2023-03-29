from binance.client import Client
from secrets_1 import api_key, api_secret
import requests

client = Client(api_key, api_secret)

class Usuario():                ## Classe que armazena dados referentes ao usuário

    def __init__(self):
        self.moeda, self.saldo_convertido, self.saldo = self.verificar_moeda_atual()
        self.trades = None
        self.orders = None
        self.client = client
        self.pares = ['BNBETH','SOLBNB','ADABNB','ADAETH','SOLETH']
        self.negociaveis = self.verificar_negociaveis(self.moeda)


    def verificar_moeda_atual(self):

        def converter(moeda):

            symbol = moeda + 'USDT'
            url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
            response = requests.get(url)

            if response.status_code == 200:
                price = response.json()['price']
                saldo_convertido = float(ativo["free"]) * float(price)
                return saldo_convertido

        info = client.get_account()
        lista_ativo = info["balances"]
        moeda = []
        saldo_convertido = []
        saldo = []

        for ativo in lista_ativo:
            if float(ativo["free"]) > 0:
                moeda.append(ativo["asset"])
                saldo_convertido.append(converter(ativo["asset"]))
                saldo.append(float(ativo["free"]))

            if saldo_convertido[-1] is None:
                del saldo_convertido[-1], moeda[-1], saldo[-1]

        maior_valor = max(saldo_convertido)
        indice_maior_valor = saldo_convertido.index(maior_valor)

        return moeda[indice_maior_valor], saldo_convertido[indice_maior_valor], saldo[indice_maior_valor]
    
    def consultar_trade(self):
        
        for moeda in self.pares:
            self.trades = self.client.get_my_trades(symbol=moeda, limit=1)


    def consultar_order(self):
        from time import sleep
       
        for moeda in self.pares:
            self.order = self.client.get_all_orders(symbol=moeda, limit=1)

            if 'LIMIT' in self.order[0]["type"]:
                while 'NEW' in self.order[0]["status"]:
                    print("Ordem ativa... \n", self.order)
                    sleep(60)

    def verificar_negociaveis(self, moeda):

        array_negociaveis = []
        for par in self.pares:

            if moeda in par:
                array_negociaveis.append(par)
        return array_negociaveis
                    
    def verificar_gatilhos(self, moeda, quantity, gatilho, objeto_moeda):
        from trade import Trade
        if moeda in self.negociaveis:
            if gatilho == 'BUY':
                return Trade.comprar(moeda, quantity, objeto_moeda)
            if gatilho == 'SELL':
                return Trade.vender(moeda, self.saldo, objeto_moeda)

    def atualizar_valores(self):
        self.moeda, self.saldo_convertido, self.saldo = self.verificar_moeda_atual()