def dados_relatorio():

    import csv

    with open('relatorio_trade.txt', 'r') as dados:
        dado = csv.reader(dados, delimiter = ",")

        for linha in dado:
            ultimo_trade_moeda = dict(linha)
            print(ultimo_trade_moeda)
            ultimo_trade = linha[12][9:15]
            ultimo_preco = linha[14][22:32]
            ultima_qty_par_1 = float(linha[7][17:-1])
            ultima_qty_par_2 = float(linha[8][25:-1])


    return ultimo_trade_moeda, ultimo_trade, ultimo_preco, ultima_qty_par_1, ultima_qty_par_2
