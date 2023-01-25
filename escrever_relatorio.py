

def relatorio(hora_atual, cotacao, cotacao2, cotacao3, posicionado):

    relatorio = open("relatorio.txt", "a+")
    relatorio.write(f"{hora_atual}, {cotacao}, {cotacao2}, {cotacao3}, {posicionado}\n")

    print("\nHora atual, Cotação BNB, Cotação SOL, Cotação ADA, Posição")
    print(f"{hora_atual}, {cotacao}, {cotacao2}, {cotacao3}, {posicionado}\n")
    relatorio.close()

def relatorio_trade(order):

    relatorio_order = open('relatorio_trade.txt', "a+")
    relatorio_order.write(f"{order}\n")
    relatorio_order.close()

def guardar_cotacao(cotacao_outro_par):

    relatorio_cotacao = open('relatorio_cotacao.txt', 'a+')
    relatorio_cotacao.write(f"{cotacao_outro_par}\n")
    relatorio_cotacao.close()

def acessar_cotacao():
    relatorio_cotacao = open('relatorio_cotacao.txt', 'r')
    for cotacao in relatorio_cotacao:
        ultima_cotacao = float(cotacao)
    relatorio_cotacao.close()
    return ultima_cotacao

    