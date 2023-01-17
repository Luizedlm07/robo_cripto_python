def bnb_eth_compram(moeda, moeda_atual, arr_ma14, arr_ma36, valor_atual, saldo):

    import trade
    from escrever_relatorio import relatorio_trade, guardar_cotacao
    from main import valor_compra
    from cotacao import cotacao
    from variaveis import cotacao_outro_par

    comprado = 0

    if moeda == 'BNBETH' and moeda_atual == 'BNB':

        if arr_ma14[-2] > arr_ma36[-2] and arr_ma14[-1] < arr_ma36[-1]:
            order = trade.vender()
            print(order)
            relatorio_trade(order)

    elif arr_ma14[-2] < arr_ma36[-2] and arr_ma14[-1] > arr_ma36[-1]:
        
        order = trade.comprar(moeda, moeda_atual, saldo)
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
                _, _, cotacao_outro_par = cotacao('SOLBNB')
        comprado = 1

        guardar_cotacao(cotacao_outro_par)
        print(order)
        relatorio_trade(order)

    else:

        print("Não comprou.")

    return valor_compra, comprado, cotacao_outro_par



def trade_sol(valor_atual, saldo):

    from escrever_relatorio import relatorio_trade
    from main import ultima_moeda
    import trade


    if ultima_moeda == 'ETH':      

        order = trade.vender('SOLETH', saldo, valor_atual)
        print(order)
        relatorio_trade(order)

    elif ultima_moeda == 'BNB':

        order = trade.vender('SOLBNB', saldo, valor_atual)
        print(order)
        relatorio_trade(order)
    


def trade_ada(valor_atual, saldo):

    from escrever_relatorio import relatorio_trade
    from main import ultima_moeda
    import trade

    # cotacao_outro_par = acessar_cotacao()

    if ultima_moeda == 'ETH':

        order = trade.vender('ADAETH', saldo, valor_atual)
        print(order)
        relatorio_trade(order)

    if ultima_moeda == 'BNB':

        order = trade.vender('ADABNB', saldo, valor_atual)
        print(order)
        relatorio_trade(order)
