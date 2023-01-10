import csv

with open('relatorio_trade.txt', 'r') as dados:
    dado = csv.reader(dados, delimiter = ",")

    for linha in dado:
        ultimo_trade_moeda = linha[0][12:18]
        ultimo_trade = linha[12][9:15]


# dado.close()
