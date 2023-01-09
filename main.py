import datetime
import time
from binance.client import Client
from secrets_1 import api_key, api_secret
from cotacao import cotacao
from escrever_relatorio import relatorio
from meu_saldo import saldo
from variaveis import *

client = Client(api_key, api_secret)

relatorio_1 = open('relatorio.txt', 'w')
relatorio_1.write("Hora atual, Cotação BNB, Cotação SOL, Cotação ADA, Posição, Lucro, Porcentagem de lucro, Lucro total\n")
relatorio_1.close()

print("Robô iniciado.\n")


while True:
    import condicao_trade
    
    hora_atual = datetime.datetime.now()
    hora_atual = (f"{hora_atual.hour}:{hora_atual.minute}:{hora_atual.second}")

    print(hora_atual, "\n")
    ma14_bnbETH, ma36_bnbETH, valor_atual_bnbETH = cotacao(bnbETH)
    ma14_solBNB, ma36_solBNB, valor_atual_solBNB = cotacao(solBNB)
    ma14_solETH, ma36_solETH, valor_atual_solETH = cotacao(solETH)
    ma14_adaBNB, ma36_adaBNB, valor_atual_adaBNB = cotacao(adaBNB)
    ma14_adaETH, ma36_adaETH, valor_atual_adaETH = cotacao(adaETH)


    saldoBNB, saldoETH, saldoADA, saldoSOL, moeda_atual = saldo()

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

    if cont < 1:
        ultima_moeda = moeda_atual
        if moeda_atual == 'ETH':
            valor_compra = valor_atual_bnbETH
        if moeda_atual == 'SOL':
            valor_compra = valor_atual_solBNB
        if moeda_atual == 'ADA':
            valor_compra = valor_atual_adaBNB

    if cont > 1:

        if moeda_atual == 'BNB':

            for moeda in pares_bnb:

                if comprado == 0:

                    valor_compra, comprado = condicao_trade.bnb_eth_compram(
                    moeda,
                    arr_ma14_bnbETH,
                    arr_ma36_bnbETH,
                    valor_atual_bnbETH
                    )
            comprado = 0

        if moeda_atual == 'ETH':

            for moeda in pares_eth:

                if comprado == 0:

                    valor_compra, comprado = condicao_trade.bnb_eth_compram(
                    moeda,
                    arr_ma14_bnbETH,
                    arr_ma36_bnbETH,
                    valor_atual_bnbETH
                    )
            comprado = 0

        if moeda_atual == 'SOL':

            lucro, lucro_porcentagem = condicao_trade.trade_sol(
            saldoSOL,
            valor_compra,
            valor_atual_solBNB,
            arr_ma14_solBNB,
            arr_ma36_solBNB,
            arr_ma14_solETH,
            arr_ma36_solETH
            )

        if moeda_atual == 'ADA':

            moeda_atual = 'ADABNB'
            lucro, lucro_porcentagem = condicao_trade.trade_ada(
            moeda_atual, 
            saldoADA,
            valor_compra,
            valor_atual_adaBNB,
            arr_ma14_adaBNB,
            arr_ma36_adaBNB,
            arr_ma14_adaETH,
            arr_ma36_adaETH
            )     

    lucro_total += lucro

    cont += 1

    relatorio(
    hora_atual=hora_atual, 
    cotacao=valor_atual_bnbETH, 
    cotacao2=valor_atual_solBNB,
    cotacao3=valor_atual_adaBNB,
    posicionado=moeda_atual,
    lucro=lucro,
    lucro_porcentagem=lucro_porcentagem,
    lucro_total=lucro_total
    )

    print("O código rodou:", cont, "vez(es).")

    time.sleep(60)
