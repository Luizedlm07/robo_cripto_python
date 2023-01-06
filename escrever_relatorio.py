

def relatorio(hora_atual, cotacao, posicionado, lucro, lucro_porcentagem, lucro_total):

    relatorio = open("relatorio.txt", "a+")
    relatorio.write(f"{hora_atual}, {cotacao}, {posicionado}, {lucro}, {lucro_porcentagem}, {lucro_total}\n")

    print("\nHora atual, Cotação, Posicionado?, Lucro, Porcentagem de lucro, Lucro total")
    print(f"{hora_atual}, {cotacao}, {posicionado}, {lucro}, {lucro_porcentagem}, {lucro_total}\n")
    relatorio.close()