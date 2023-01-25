def dados_relatorio():

    import csv

    with open('relatorio_trade.txt', 'r') as dados:
        dado = csv.reader(dados, delimiter = ",")

        for linha in dado:

            if 'MARKET' in linha[11]:

                ultimo_trade_moeda = linha[0][12:18]
                ultimo_trade = linha[12][9:15]
                ultimo_preco = linha[14][22:32]

            elif 'LIMIT' in linha[11]:
                
                ultimo_trade_moeda = linha[0][12:18]
                ultimo_trade = linha[11][9:15]
                ultimo_preco = linha[4][11:20]

    return ultimo_trade_moeda, ultimo_trade, ultimo_preco
