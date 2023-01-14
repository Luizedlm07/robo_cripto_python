def saldo():

    from secrets_1 import api_key, api_secret
    from binance.client import Client
    client = Client(api_key, api_secret)

    from variaveis import minhas_moedas
    from dados_relatorio import dados_relatorio

    info = client.get_account()

    lista_ativo = info["balances"]


    for ativo in lista_ativo:
        if float(ativo["free"]) > 0 or ativo["asset"] == 'SOL' or ativo["asset"] == 'ADA':
            minhas_moedas.append(ativo)


    meu_saldoBNB = float(minhas_moedas[2]['free'])
    meu_saldoETH = float(minhas_moedas[1]['free'])
    meu_saldoADA = float(minhas_moedas[3]['free'])
    meu_saldoSOL = float(minhas_moedas[5]['free'])

    ultimo_trade_moeda, ultimo_trade, ultimo_preco, ultima_qty_par_1, ultima_qty_par_2 = dados_relatorio()

    moeda_atual = ultimo_trade_moeda[:3] if 'BUY' in ultimo_trade else ultimo_trade_moeda[3:]

    del minhas_moedas[0:]

    return meu_saldoBNB, meu_saldoETH, meu_saldoADA, meu_saldoSOL, moeda_atual, ultimo_trade_moeda, ultimo_preco
