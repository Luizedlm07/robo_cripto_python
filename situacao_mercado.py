from trade import Trade

class Situacao_Mercado():

    def __init__(self, objeto_moeda, objeto_usuario):
        self.pares = ['BNBETH','SOLBNB','ADABNB','ADAETH','SOLETH']
        self.negociaveis = self.verificar_negociaveis(objeto_usuario.moeda)
        self.order = self.gatilho_trade(objeto_moeda, objeto_usuario)
        

    def verificar_negociaveis(self, moeda):

        array_negociaveis = []
        for par in self.pares:

            if moeda in par:
                array_negociaveis.append(par)
        return array_negociaveis

    def gatilho_trade(self, objeto_moeda, objeto_usuario):        ## Se a minha moeda atual for igual a primeira moeda do par, ela pode vender. Se for igual a segunda moeda, pode comprar

        for par in self.negociaveis:
            if objeto_usuario.moeda == par[:2]:
                if objeto_moeda.lista_mm_menor[-1] < objeto_moeda.lista_mm_maior[-1] and objeto_moeda.lista_mm_menor[-2] > objeto_moeda.lista_mm_maior[-2]:
                        order = Trade.vender(par, objeto_usuario.saldo)
                        return order
                
            if objeto_usuario.moeda == par[-3:]:
                if objeto_moeda.lista_mm_menor[-1] > objeto_moeda.lista_mm_maior[-1] and objeto_moeda.lista_mm_menor[-2] < objeto_moeda.lista_mm_maior[-2]:
                        order = Trade.comprar(par, objeto_usuario.saldo)
                        return order
