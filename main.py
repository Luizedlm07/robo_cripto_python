import datetime
import time
from escrever_relatorio import Relatorio
from binance import exceptions
from class_usuario import Usuario
usuario = Usuario()
from par_moeda import Par_moeda
from situacao_mercado import Situacao_Mercado




print("Robô iniciado.\n")

Relatorio()

bnbETH = Par_moeda('BNBETH')
solBNB = Par_moeda('SOLBNB')
solETH = Par_moeda('SOLETH')
adaBNB = Par_moeda('ADABNB')
adaETH = Par_moeda('ADAETH')

contador = 0

while True:
    try:

        hora_atual = datetime.datetime.now()
        hora_atual = (f"{hora_atual.hour}:{hora_atual.minute}:{hora_atual.second}")
        print(hora_atual)

        bnbETH.atualizar_valores(bnbETH.symbol)
        solBNB.atualizar_valores(solBNB.symbol)
        solETH.atualizar_valores(solETH.symbol)
        adaBNB.atualizar_valores(adaBNB.symbol)
        adaETH.atualizar_valores(adaETH.symbol)

        print(f'Posição: {usuario.moeda}')
        print(f'Saldo: {usuario.saldo_convertido:.2f} US$\n')
        
        if contador < 3:
            contador += 1
            continue
        
        print(f"Média Móvel {bnbETH.symbol} | Menor = {bnbETH.mm_menor:.8f} | Maior = {bnbETH.mm_maior:.8f}")
        print(f"Média Móvel {solBNB.symbol} | Menor = {solBNB.mm_menor:.8f} | Maior = {solBNB.mm_maior:.8f}")
        print(f"Média Móvel {adaBNB.symbol} | Menor = {adaBNB.mm_menor:.8f} | Maior = {adaBNB.mm_maior:.8f}")
        print(f"Média Móvel {solETH.symbol} | Menor = {solETH.mm_menor:.8f} | Maior = {solETH.mm_maior:.8f}")
        print(f"Média Móvel {adaETH.symbol} | Menor = {adaETH.mm_menor:.8f} | Maior = {adaETH.mm_maior:.8f}")

        mercado_bnbeth = Situacao_Mercado(bnbETH)
        mercado_solbnb = Situacao_Mercado(solBNB)
        mercado_adabnb = Situacao_Mercado(adaBNB)
        mercado_soleth = Situacao_Mercado(solETH)
        mercado_adaeth = Situacao_Mercado(adaETH)

        usuario.atualizar_valores()
        usuario.consultar_order()
        usuario.consultar_trade()
        
        Relatorio.relatorio_constante(
        hora_atual=hora_atual, 
        cotacao=bnbETH.cotacao, 
        cotacao2=solBNB.cotacao,
        cotacao3=adaBNB.cotacao,
        cotacao4=solETH.cotacao,
        cotacao5=adaETH.cotacao,
        posicionado=usuario.moeda
        )

        contador += 1
        print("O código rodou:", contador, "vez(es).\n")

        time.sleep(61)

    except exceptions.BinanceRequestException as erro:
        
        print(erro)
        time.sleep(300)