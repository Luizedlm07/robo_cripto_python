def condition_tradeBNB(moeda, arr_ma14, arr_ma36, valor_atual):

    import trade
    from escrever_relatorio import relatorio_trade

    valor_compra = 0
    comprado = 0

    if arr_ma14[-2] < arr_ma36[-2] and arr_ma14[-1] > arr_ma36[-1]:
        
        order = trade.comprar(moeda)
        valor_compra = valor_atual
        comprado = 1
        relatorio_trade()
        print(order)

    else:

        print("Não comprou.\n")

    return valor_compra, comprado, order


def condition_trade(moeda, valor_compra, valor_atual):
    
    from escrever_relatorio import relatorio_trade
    from variaveis import lucro, lucro_porcentagem
    import trade


    if valor_atual > valor_compra * 1.005:

        order = trade.vender(moeda)
        relatorio_trade()
        print(order)

        lucro = valor_atual - valor_compra
        lucro_porcentagem = lucro / valor_compra * 100
    
    return lucro, lucro_porcentagem, order

