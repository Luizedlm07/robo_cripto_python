

def condition_trade(moeda, cont, arr_ma14, arr_ma36, valor_atual, comprar, vender):
    from variaveis import lucro, lucro_porcentagem, lucro_total
    import trade
    if cont > 1 and comprar == True:

        if arr_ma14[-2] < arr_ma36[-2] and arr_ma14[-1] > arr_ma36[-1]:

            order = trade.comprar(moeda)

            print(order)

            comprar = False
            valor_compra = valor_atual

        else:
            print("Não comprou.\n")

    if cont > 1 and vender == True:

        if valor_atual > valor_compra * 1.005:

            order = trade.vender(moeda)
            print(order)

            vender = False
            lucro = valor_atual - valor_compra
            lucro_porcentagem = lucro / valor_compra * 100
    
    return lucro, lucro_porcentagem
