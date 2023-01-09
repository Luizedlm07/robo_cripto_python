def saldo():

    from main import client
    from variaveis import minhas_moedas

    info = client.get_account()

    lista_ativo = info["balances"]


    for ativo in lista_ativo:
        if float(ativo["free"]) > 0 or ativo["asset"] == 'SOL' or ativo["asset"] == 'ADA':
            minhas_moedas.append(ativo)


    meu_saldoBNB = float(minhas_moedas[2]['free'])
    meu_saldoETH = float(minhas_moedas[1]['free'])
    meu_saldoADA = float(minhas_moedas[3]['free'])
    meu_saldoSOL = float(minhas_moedas[5]['free'])

    lista_saldos = [meu_saldoBNB, meu_saldoETH, meu_saldoADA, meu_saldoSOL]

    maior_saldo = 0
    moeda_atual = ''

    comprar = False
    vender = False

    for saldo in lista_saldos:
        maior_saldo = saldo if saldo > maior_saldo else maior_saldo

    if maior_saldo == meu_saldoETH:
        moeda_atual = 'ETH'

    if maior_saldo == meu_saldoBNB:
        moeda_atual = 'BNB'

    if maior_saldo == meu_saldoADA:
        moeda_atual = 'ADA'

    if maior_saldo == meu_saldoSOL:
        moeda_atual = 'SOL'

    return meu_saldoBNB, meu_saldoETH, meu_saldoADA, meu_saldoSOL, moeda_atual