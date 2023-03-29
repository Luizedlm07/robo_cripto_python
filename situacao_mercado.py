class Situacao_Mercado():

    def __init__(self, objeto_moeda):
      self.gatilho_trade(objeto_moeda)

    def gatilho_trade(self, objeto_moeda):
      from main import usuario
      from escrever_relatorio import Relatorio

      if usuario.moeda == objeto_moeda.symbol[-3:]:

        if objeto_moeda.lista_mm_menor[-1] < objeto_moeda.lista_mm_maior[-1] and objeto_moeda.lista_mm_menor[-2] > objeto_moeda.lista_mm_maior[-2]:
          print(f'Gatilho de compra para {objeto_moeda.symbol}')
          order = usuario.verificar_gatilhos(objeto_moeda.symbol, self.converter(objeto_moeda.symbol), 'BUY', objeto_moeda)
          if order is not None:
            Relatorio.relatorio_trade(order)
      
      if usuario.moeda == objeto_moeda.symbol[:2]:

        if objeto_moeda.lista_mm_menor[-1] > objeto_moeda.lista_mm_maior[-1] and objeto_moeda.lista_mm_menor[-2] < objeto_moeda.lista_mm_maior[-2]:
          print(f'Gatilho de venda para {objeto_moeda.symbol}')
          order = usuario.verificar_gatilhos(objeto_moeda.symbol, self.converter(objeto_moeda.symbol),'SELL', objeto_moeda)      
          if order is not None:
            Relatorio.relatorio_trade(order)

    def converter(self, symbol):
      from main import usuario
      import requests

      url = f'https://api.binance.com/api/v3/ticker/price?symbol={symbol}'
      response = requests.get(url)

      if response.status_code == 200:
          price = response.json()['price']
          quantity = usuario.saldo * float(price)
          print('Quantity: ', quantity)
          return quantity
      

## Adicionadas condições para gerar gatilho de compra ou venda, baseado na posição
## do nome da moeda no par, exemplo:
## BNBETH >> se eu tiver BNB só posso vender, se eu tiver ETH, só posso comprar.

