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
    import cond_totrade
    ma14_bnb, ma36_bnb, valor_atual_bnb = cotacao(bnbETH)
    ma14_sol, ma36_sol, valor_atual_sol = cotacao(solBNB)
    ma14_ada, ma36_ada, valor_atual_ada = cotacao(adaBNB)

    hora_atual = datetime.datetime.now()
    hora_atual = (f"{hora_atual.hour}:{hora_atual.minute}:{hora_atual.second}")

    print(hora_atual)

    saldoBNB, saldoETH, saldoADA, saldoSOL, moeda_atual, comprar, vender = saldo()

    print("Meus ativos: " )
    print("Meu saldo BNB = ", saldoBNB)
    print("Meu saldo ETH = ", saldoETH,)
    print("Meu saldo ADA = ", saldoADA,)
    print("Meu saldo SOL = ", saldoSOL,)

    arr_ma14_bnb.append(ma14_bnb)
    arr_ma36_bnb.append(ma36_bnb)
    arr_ma14_sol.append(ma14_sol)
    arr_ma36_sol.append(ma36_sol)
    arr_ma14_ada.append(ma14_ada)
    arr_ma36_ada.append(ma36_ada)

    if cont < 1:
        if moeda_atual == 'ETH':
            valor_compra = valor_atual_bnb
        if moeda_atual == 'SOL':
            valor_compra = valor_atual_sol
        if moeda_atual == 'ADA':
            valor_compra = valor_atual_ada

    if cont > 1:

        if moeda_atual == 'BNB':

            for moeda in lista_moedas:

                if comprado == 0:

                    valor_compra, comprado = cond_totrade.condition_tradeBNB(
                    moeda,
                    arr_ma14_bnb,
                    arr_ma36_bnb,
                    valor_atual_bnb
                    )

        if moeda_atual == 'ETH':

            moeda_atual = 'BNBETH'
            lucro, lucro_porcentagem = cond_totrade.condition_trade(
            moeda_atual, 
            valor_compra,
            valor_atual_bnb
            )

        if moeda_atual == 'SOL':

            moeda_atual = 'SOLBNB'
            lucro, lucro_porcentagem = cond_totrade.condition_trade(
            moeda_atual, 
            valor_compra,
            valor_atual_sol
            )

        if moeda_atual == 'ADA':

            moeda_atual = 'ADABNB'
            lucro, lucro_porcentagem = cond_totrade.condition_trade(
            moeda_atual, 
            valor_compra,
            valor_atual_ada
            )     

    lucro_total += lucro

    cont += 1

    print("O código rodou:", cont, "vez(es).")

    relatorio(
    hora_atual=hora_atual, 
    cotacao=valor_atual_bnb, 
    cotacao2=valor_atual_sol,
    cotacao3=valor_atual_ada,
    posicionado=moeda_atual,
    lucro=lucro,
    lucro_porcentagem=lucro_porcentagem,
    lucro_total=lucro_total
    )

    time.sleep(60)
