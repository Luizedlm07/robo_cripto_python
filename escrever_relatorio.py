class Relatorio():

    def __init__(self):
        self.primeira_linha = open('relatorio.txt', 'w')
        self.primeira_linha.write("Hora atual, BNBETH, SOLBNB, ADABNB, SOLETH, ADABNB, Posição\n")
        self.primeira_linha.close()

    @classmethod
    def relatorio_constante(self,hora_atual, cotacao, cotacao2, cotacao3, cotacao4, cotacao5, posicionado):

        relatorio = open("relatorio.txt", "a+")
        relatorio.write(f"{hora_atual}, {cotacao}, {cotacao2}, {cotacao3}, {posicionado}\n")
        print("\nCotações:")
        print("\nHora atual, BNBETH, SOLBNB, ADABNB, SOLETH, ADAETH,  Posição")
        print(f"{hora_atual}, {cotacao}, {cotacao2}, {cotacao3}, {cotacao4}, {cotacao5}, {posicionado}\n")
        relatorio.close()

    @classmethod
    def relatorio_trade(self, order):

        relatorio_order = open('relatorio_trade.txt', "a+")
        relatorio_order.write(f"{order}\n")
        relatorio_order.close()


    