

def relatorio(hora_atual, cotacao, cotacao2, cotacao3, posicionado):

    relatorio = open("relatorio.txt", "a+")
    relatorio.write(f"{hora_atual}, {cotacao}, {cotacao2}, {cotacao3}, {posicionado}\n")

    print("\nHora atual, Cotação BNB, Cotação SOL, Cotação ADA, Posição")
    print(f"{hora_atual}, {cotacao}, {cotacao2}, {cotacao3}, {posicionado}\n")
    relatorio.close()

def relatorio_trade(order):

    relatorio_order = open('relatorio_trade.txt', "a+")
    relatorio_order.write(f"\n{order}")
    relatorio_order.close()
