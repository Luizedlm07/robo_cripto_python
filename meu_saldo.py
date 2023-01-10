def saldo():

    from main import client
    from variaveis import minhas_moedas
    from dados_relatorio import ultimo_trade, ultimo_trade_moeda

    info = client.get_account()

    lista_ativo = info["balances"]


    for ativo in lista_ativo:
        if float(ativo["free"]) > 0 or ativo["asset"] == 'SOL' or ativo["asset"] == 'ADA':
            minhas_moedas.append(ativo)


    meu_saldoBNB = float(minhas_moedas[2]['free'])
    meu_saldoETH = float(minhas_moedas[1]['free'])
    meu_saldoADA = float(minhas_moedas[3]['free'])
    meu_saldoSOL = float(minhas_moedas[5]['free'])

    moeda_atual = ultimo_trade_moeda[:3] if 'BUY' in ultimo_trade else ultimo_trade_moeda[3:]

    return meu_saldoBNB, meu_saldoETH, meu_saldoADA, meu_saldoSOL, moeda_atual