import csv

with open('relatorio_trade.txt', 'r') as dados:
    dado = csv.reader(dados, delimiter = ",")

    for linha in dado:
        ultimo_trade = linha[0][11:20]

# dado.close()
