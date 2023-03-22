import datetime
import time

from escrever_relatorio import relatorio, relatorio_trade
from variaveis import *
from binance import exceptions

from class_usuario import Usuario
usuario = Usuario()

from par_moeda import Par_moeda
from situacao_mercado import Situacao_Mercado
from trade import Trade


relatorio_1 = open('relatorio.txt', 'w')
relatorio_1.write("Hora atual, Cotação BNB, Cotação SOL, Cotação ADA, Posição, Lucro, Porcentagem de lucro, Lucro total\n")
relatorio_1.close()

print("Robô iniciado.\n")

bnbETH = Par_moeda('BNBETH')
solBNB = Par_moeda('SOLBNB')
solETH = Par_moeda('SOLETH')
adaBNB = Par_moeda('ADABNB')
adaETH = Par_moeda('ADAETH')


while True:
    try:

        hora_atual = datetime.datetime.now()
        hora_atual = (f"{hora_atual.hour}:{hora_atual.minute}:{hora_atual.second}")
        print(hora_atual, "\n")

        bnbETH.verificar_medias_moveis(bnbETH.symbol)
        solBNB.verificar_medias_moveis(solBNB.symbol)
        solETH.verificar_medias_moveis(solETH.symbol)
        adaBNB.verificar_medias_moveis(adaBNB.symbol)
        adaETH.verificar_medias_moveis(adaETH.symbol)

        print(f'Posição: {usuario.moeda}')
        print(f'Saldo: {usuario.saldo:.2f}US$')
        
        if cont < 3:
            cont += 1
            continue


        
        for moeda in lista_moedas:

            orders = usuario.client.get_all_orders(symbol=moeda, limit=1)

            if 'LIMIT' in orders[0]["type"]:

                while 'NEW' in orders[0]["status"]:

                    print("Ordem ativa... \n", orders)
                    time.sleep(60)

                if 'FILLED' in orders[0]["status"]:
                    print('Trade concluído!\n', orders)
                    relatorio_trade(orders)

        mercado_bnbeth = Situacao_Mercado(bnbETH, usuario)
        mercado_solbnb = Situacao_Mercado(solBNB, usuario)
        mercado_adabnb = Situacao_Mercado(adaBNB, usuario)
        mercado_soleth = Situacao_Mercado(solETH, usuario)
        mercado_adaeth = Situacao_Mercado(adaETH, usuario)




        valor_compra = float(ultimo_preco)
        ultima_moeda = 'BNB' if 'BNB' in ultimo_trade_moeda else 'ETH'

        print("Ultima moeda: ", ultima_moeda)

        if cont > 1:

            if moeda_atual == 'BNB':

                for moeda in pares_bnb:

                    if comprado == 0 and moeda == 'BNBETH':

                        valor_compra, comprado, cotacao_outro_par = condicao_trade.bnb_eth_compram(
                        moeda,
                        moeda_atual,
                        arr_ma14_bnbETH,
                        arr_ma36_bnbETH,
                        valor_atual_bnbETH,
                        saldoBNB
                        )

                    if comprado == 0 and moeda == 'SOLBNB':

                        valor_compra, comprado, cotacao_outro_par = condicao_trade.bnb_eth_compram(
                        moeda,
                        moeda_atual,
                        arr_ma14_solBNB,
                        arr_ma36_solBNB,
                        valor_atual_solBNB,
                        saldoBNB
                        )

                    if comprado == 0 and moeda == 'ADABNB':

                        valor_compra, comprado, cotacao_outro_par = condicao_trade.bnb_eth_compram(
                        moeda,
                        moeda_atual,
                        arr_ma14_adaBNB,
                        arr_ma36_adaBNB,
                        valor_atual_adaBNB,
                        saldoBNB
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
                        valor_atual_bnbETH,
                        saldoETH
                        )

                    if comprado == 0 and moeda == 'SOLETH':

                        valor_compra, comprado, cotacao_outro_par = condicao_trade.bnb_eth_compram(
                        moeda,
                        moeda_atual,
                        arr_ma14_solETH,
                        arr_ma36_solETH,
                        valor_atual_solETH,
                        saldoETH
                        )

                    if comprado == 0 and moeda == 'ADAETH':

                        valor_compra, comprado = condicao_trade.bnb_eth_compram(
                        moeda,
                        moeda_atual,
                        arr_ma14_adaETH,
                        arr_ma36_adaETH,
                        valor_atual_adaETH,
                        saldoETH
                        )

                comprado = 0

            if moeda_atual == 'SOL':

                condicao_trade.trade_sol(
                valor_atual_solBNB,
                saldoSOL
                )

            if moeda_atual == 'ADA':

                condicao_trade.trade_ada(
                valor_atual_adaBNB,
                saldoADA
                )     

        lucro_total += lucro

        relatorio(
        hora_atual=hora_atual, 
        cotacao=valor_atual_bnbETH, 
        cotacao2=valor_atual_solBNB,
        cotacao3=valor_atual_adaBNB,
        posicionado=moeda_atual
        )

        print("O código rodou:", cont, "vez(es).")

        time.sleep(61)

    except exceptions.BinanceRequestException as erro:
        
        print(erro)
        time.sleep(300)