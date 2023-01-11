def bnb_eth_compram(moeda, moeda_atual, arr_ma14, arr_ma36, valor_atual):

    import trade
    from escrever_relatorio import relatorio_trade
    from main import valor_compra
    from cotacao import cotacao

    comprado = 0

    if arr_ma14[-2] < arr_ma36[-2] and arr_ma14[-1] > arr_ma36[-1]:
        
        order = trade.comprar(moeda, moeda_atual)
        valor_compra = valor_atual
        if 'BNB' in moeda:
            if 'ADA' in moeda:
                _, _, cotacao_outro_par = cotacao('ADAETH')
            if 'SOL' in moeda:
                _, _, cotacao_outro_par = cotacao('SOLETH')
        if 'ETH' in moeda:
            if 'ADA' in moeda:
                _, _, cotacao_outro_par = cotacao('ADABNB')
            if 'SOL' in moeda:
                _, _, cotacao_outro_par = cotacao('ADABNB')
        comprado = 1
        
        print(order)
        relatorio_trade(order)

    else:

        print("Não comprou.")

    return valor_compra, comprado, cotacao_outro_par



def trade_sol(valor_compra, valor_atual):

    from escrever_relatorio import relatorio_trade
    from main import ultima_moeda, valor_atual_adaBNB, valor_atual_adaETH, cotacao_outro_par
    import trade


    if ultima_moeda == 'ETH':
        
        if valor_atual > valor_compra * 1.0025:

            order = trade.vender('SOLETH')
            print(order)
            relatorio_trade(order)

        if valor_atual_adaBNB > cotacao_outro_par * 1.0025:
            
            order = trade.vender('SOLBNB')
            
            print(order)
            relatorio_trade(order)

    if ultima_moeda == 'BNB':

        if valor_atual > valor_compra * 1.0025:

            order = trade.vender('SOLBNB')
            print(order)
            relatorio_trade(order)

        if valor_atual_adaETH > cotacao_outro_par * 1.0025:
            
            order = trade.vender('SOLETH')
            
            print(order)
            relatorio_trade(order)
    


def trade_ada(valor_compra, valor_atual):

    from escrever_relatorio import relatorio_trade
    from main import ultima_moeda, valor_atual_adaBNB, valor_atual_adaETH, cotacao_outro_par
    import trade


    if ultima_moeda == 'ETH':
        
        if valor_atual > valor_compra * 1.0025:

            order = trade.vender('ADAETH')
            print(order)
            relatorio_trade(order)

        if valor_atual_adaBNB > cotacao_outro_par * 1.0025:
            
            order = trade.vender('ADABNB')
            
            print(order)
            relatorio_trade(order)

    if ultima_moeda == 'BNB':

        if valor_atual > valor_compra * 1.0025:

            order = trade.vender('ADABNB')
            print(order)
            relatorio_trade(order)

        if valor_atual_adaETH > cotacao_outro_par * 1.0025:
            
            order = trade.vender('ADAETH')
            
            print(order)
            relatorio_trade(order)
    