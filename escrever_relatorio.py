

def relatorio(hora_atual, cotacao, cotacao2, cotacao3, posicionado, lucro, lucro_porcentagem, lucro_total):

    relatorio = open("relatorio.txt", "a+")
    relatorio.write(f"{hora_atual}, {cotacao}, {cotacao2}, {cotacao3}, {posicionado}, {lucro}, {lucro_porcentagem}, {lucro_total}\n")

    print("\nHora atual, Cotação BNB, Cotação SOL, Cotação ADA, Posicionado?, Lucro, Porcentagem de lucro, Lucro total")
    print(f"{hora_atual}, {cotacao}, {cotacao2}, {cotacao3}, {posicionado}, {lucro}, {lucro_porcentagem}, {lucro_total}\n")
    relatorio.close()