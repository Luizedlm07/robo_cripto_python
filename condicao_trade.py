def bnb_eth_compram(moeda, arr_ma14, arr_ma36, valor_atual):

    import trade
    from escrever_relatorio import relatorio_trade
    from main import valor_compra

    comprado = 0

    if arr_ma14[-2] < arr_ma36[-2] and arr_ma14[-1] > arr_ma36[-1]:
        
        order = trade.comprar(moeda)
        valor_compra = valor_atual
        comprado = 1
        
        print(order)
        relatorio_trade(order)

    else:

        print("Não comprou.\n")

    return valor_compra, comprado






def trade_sol(saldo, valor_compra, valor_atual, arr_ma14BNB, arr_ma36BNB, arr_ma14ETH, arr_ma36ETH):

    from escrever_relatorio import relatorio_trade
    from variaveis import lucro, lucro_porcentagem, pares_sol
    from main import ultima_moeda
    import trade


    if ultima_moeda == 'ETH':

        if valor_atual > valor_compra * 1.0025:

            order = trade.vender('SOLETH', saldo)
            print(order)
            relatorio_trade()

            lucro = valor_atual - valor_compra
            lucro_porcentagem = lucro / valor_compra * 100

        if arr_ma14BNB[-2] < arr_ma36BNB[-2] and arr_ma14BNB[-1] > arr_ma36BNB[-1]:
            
            order = trade.vender('SOLBNB')
            valor_compra = valor_atual
            
            print(order)
            relatorio_trade(order)

    if ultima_moeda == 'BNB':

        if valor_atual > valor_compra * 1.0025:

            order = trade.vender('SOLBNB', saldo)
            print(order)
            relatorio_trade()

            lucro = valor_atual - valor_compra
            lucro_porcentagem = lucro / valor_compra * 100

        if arr_ma14ETH[-2] < arr_ma36ETH[-2] and arr_ma14ETH[-1] > arr_ma36ETH[-1]:
            
            order = trade.vender('SOLETH')
            valor_compra = valor_atual
            
            print(order)
            relatorio_trade(order)

    return lucro, lucro_porcentagem





def trade_ada(saldo, valor_compra, valor_atual, arr_ma14BNB, arr_ma36BNB, arr_ma14ETH, arr_ma36ETH):

    from escrever_relatorio import relatorio_trade
    from variaveis import lucro, lucro_porcentagem, pares_sol
    from main import ultima_moeda
    import trade


    if ultima_moeda == 'ETH':

        if valor_atual > valor_compra * 1.0025:

            order = trade.vender('ADAETH', saldo)
            print(order)
            relatorio_trade()

            lucro = valor_atual - valor_compra
            lucro_porcentagem = lucro / valor_compra * 100

        if arr_ma14BNB[-2] < arr_ma36BNB[-2] and arr_ma14BNB[-1] > arr_ma36BNB[-1]:
            
            order = trade.vender('ADABNB')
            valor_compra = valor_atual
            
            print(order)
            relatorio_trade(order)

    if ultima_moeda == 'BNB':

        if valor_atual > valor_compra * 1.0025:

            order = trade.vender('SOLBNB', saldo)
            print(order)
            relatorio_trade()

            lucro = valor_atual - valor_compra
            lucro_porcentagem = lucro / valor_compra * 100

        if arr_ma14ETH[-2] < arr_ma36ETH[-2] and arr_ma14ETH[-1] > arr_ma36ETH[-1]:
            
            order = trade.vender('SOLETH')
            valor_compra = valor_atual
            
            print(order)
            relatorio_trade(order)
    
    return lucro, lucro_porcentagem
