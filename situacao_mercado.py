class Situacao_Mercado():

    def __init__(self, objeto_moeda):
      self.gatilho_trade(objeto_moeda)

    def gatilho_trade(self, objeto_moeda):
      from main import usuario
      from escrever_relatorio import Relatorio

      if objeto_moeda.lista_mm_menor[-1] < objeto_moeda.lista_mm_maior[-1] and objeto_moeda.lista_mm_menor[-2] > objeto_moeda.lista_mm_maior[-2]:
        print(f'Gatilho de compra para {objeto_moeda.symbol}')
        order = usuario.verificar_gatilhos(objeto_moeda.symbol, 'BUY', objeto_moeda)
        if order is not None:
          Relatorio.relatorio_trade(order)
      

      if objeto_moeda.lista_mm_menor[-1] > objeto_moeda.lista_mm_maior[-1] and objeto_moeda.lista_mm_menor[-2] < objeto_moeda.lista_mm_maior[-2]:
        print(f'Gatilho de venda para {objeto_moeda.symbol}')
        usuario.verificar_gatilhos(objeto_moeda.symbol, 'SELL', objeto_moeda)
        

      

## Verificar negociáveis foi removido da classe 'Situação Mercado'
## A clase 'Situação Mercado não faz mais a chamada das funções de compra e venda
## Agora ela chama uma função da classe usuário, passando gatilhos de compra e venda
## Então, a classe Usuario é que faz a chamada das funções de compra e venda

