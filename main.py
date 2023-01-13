import datetime
import time

from secrets_1 import api_key, api_secret
from cotacao import cotacao
from escrever_relatorio import relatorio

from variaveis import *


relatorio_1 = open('relatorio.txt', 'w')
relatorio_1.write("Hora atual, Cotação BNB, Cotação SOL, Cotação ADA, Posição, Lucro, Porcentagem de lucro, Lucro total\n")
relatorio_1.close()

print("Robô iniciado.\n")


while True:
    
    from binance.client import Client
    client = Client(api_key, api_secret)
    from meu_saldo import saldo
    import condicao_trade

    

    hora_atual = datetime.datetime.now()
    hora_atual = (f"{hora_atual.hour}:{hora_atual.minute}:{hora_atual.second}")

    print(hora_atual, "\n")
    ma14_bnbETH, ma36_bnbETH, valor_atual_bnbETH = cotacao(bnbETH)
    ma14_solBNB, ma36_solBNB, valor_atual_solBNB = cotacao(solBNB)
    ma14_solETH, ma36_solETH, valor_atual_solETH = cotacao(solETH)
    ma14_adaBNB, ma36_adaBNB, valor_atual_adaBNB = cotacao(adaBNB)
    ma14_adaETH, ma36_adaETH, valor_atual_adaETH = cotacao(adaETH)


    saldoBNB, saldoETH, saldoADA, saldoSOL, moeda_atual, ultimo_trade_moeda, ultimo_preco = saldo()

    print("Meus ativos: " )
    print("Meu saldo BNB = ", saldoBNB)
    print("Meu saldo ETH = ", saldoETH)
    print("Meu saldo ADA = ", saldoADA)
    print("Meu saldo SOL = ", saldoSOL, "\n")

    arr_ma14_bnbETH.append(ma14_bnbETH)
    arr_ma36_bnbETH.append(ma36_bnbETH)
    arr_ma14_solBNB.append(ma14_solBNB)
    arr_ma36_solBNB.append(ma36_solBNB)
    arr_ma14_solETH.append(ma14_solETH)
    arr_ma36_solETH.append(ma36_solETH)
    arr_ma14_adaBNB.append(ma14_adaBNB)
    arr_ma36_adaBNB.append(ma36_adaBNB)
    arr_ma14_adaETH.append(ma14_adaETH)
    arr_ma36_adaETH.append(ma36_adaETH)

    valor_compra = float(ultimo_preco)
    ultima_moeda = 'BNB' if 'BNB' in ultimo_trade_moeda else 'ETH'

    print("Ultima moeda: ", ultima_moeda)

    if cont > 1:

        if moeda_atual == 'BNB':

            for moeda in pares_bnb:

                if comprado == 0 and moeda == 'SOLBNB':

                    valor_compra, comprado, cotacao_outro_par = condicao_trade.bnb_eth_compram(
                    moeda,
                    moeda_atual,
                    arr_ma14_solBNB,
                    arr_ma36_solBNB,
                    valor_atual_solBNB
                    )

                if comprado == 0 and moeda == 'ADABNB':

                    valor_compra, comprado, cotacao_outro_par = condicao_trade.bnb_eth_compram(
                    moeda,
                    moeda_atual,
                    arr_ma14_adaBNB,
                    arr_ma36_adaBNB,
                    valor_atual_adaBNB
                    )

            comprado = 0

        if moeda_atual == 'ETH':

            for moeda in pares_eth:

                if comprado == 0 and moeda == 'BNBETH':

                    valor_compra, comprado, cotacao_outro_par = condicao_trade.bnb_eth_compram(
                    moeda,
                    moeda_atual,
                    arr_ma14_bnbETH,
                    arr_ma36_bnbETH,
                    valor_atual_bnbETH
                    )

                if comprado == 0 and moeda == 'SOLETH':

                    valor_compra, comprado, cotacao_outro_par = condicao_trade.bnb_eth_compram(
                    moeda,
                    moeda_atual,
                    arr_ma14_solETH,
                    arr_ma36_solETH,
                    valor_atual_solETH
                    )

                if comprado == 0 and moeda == 'ADAETH':

                    valor_compra, comprado = condicao_trade.bnb_eth_compram(
                    moeda,
                    moeda_atual,
                    arr_ma14_adaETH,
                    arr_ma36_adaETH,
                    valor_atual_adaETH
                    )

            comprado = 0

        if moeda_atual == 'SOL':

            condicao_trade.trade_sol(
            valor_compra,
            valor_atual_solBNB
            )

        if moeda_atual == 'ADA':

            condicao_trade.trade_ada(
            valor_compra,
            valor_atual_adaBNB
            )     

    lucro_total += lucro

    cont += 1

    relatorio(
    hora_atual=hora_atual, 
    cotacao=valor_atual_bnbETH, 
    cotacao2=valor_atual_solBNB,
    cotacao3=valor_atual_adaBNB,
    posicionado=moeda_atual
    )

    print("O código rodou:", cont, "vez(es).")

    time.sleep(60)
