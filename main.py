import datetime
import time
from binance.client import Client
from secrets_1 import api_key, api_secret
from cotacao import cotacao
from escrever_relatorio import relatorio
import trade
from variaveis import *

client = Client(api_key, api_secret)

relatorio_1 = open('relatorio.txt', 'w')
relatorio_1.write("Hora atual, Cotação, Posicionado?, Lucro, Porcentagem de lucro, Lucro total\n")
relatorio_1.close()



print("Robô iniciado.\n")


while True:
    ma14, ma36, valor_atual = cotacao()

    info = client.get_account()

    lista_ativo = info["balances"]

    for ativo in lista_ativo:
        if float(ativo["free"]) > 0:
            minhas_moedas.append(ativo)
    
    meu_saldoBNB = float(minhas_moedas[2]['free'])
    meu_saldoETH = float(minhas_moedas[1]['free'])
    hora_atual = datetime.datetime.now()
    hora_atual = (f"{hora_atual.hour}:{hora_atual.minute}:{hora_atual.second}")

    print(hora_atual)

    print("Meus ativos: " )
    print("Meu saldo BNB = ", meu_saldoBNB)
    print("Meu saldo ETH = ", meu_saldoETH, "\n")


    arr_ma14.append(ma14)
    arr_ma36.append(ma36)

    if cont > 1 and posicionado == False:

        if arr_ma14[-2] < arr_ma36[-2] and arr_ma14[-1] > arr_ma36[-1]:

            order = trade.comprar()

            print(order)

            posicionado = True
            valor_compra = valor_atual

        else:
            print("Não comprou.\n")

    if cont > 1 and posicionado == True:

        if arr_ma36[-2] < arr_ma14[-2] and arr_ma36[-1] > arr_ma14[-1]:

            order = trade.vender()
            print(order)

            posicionado = False
            lucro = valor_atual - valor_compra
            lucro_porcentagem = lucro / valor_compra * 100
            lucro_total += lucro

    cont += 1

    print("O código rodou:", cont, "vezes.")

    relatorio(
    hora_atual=hora_atual, 
    cotacao=valor_atual, 
    posicionado=posicionado,
    lucro=lucro,
    lucro_porcentagem=lucro_porcentagem,
    lucro_total=lucro_total
    )

    time.sleep(60)
