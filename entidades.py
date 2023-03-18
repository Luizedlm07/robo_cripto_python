class Par_moeda():

    def __init__(self, symbol):
        self.symbol = symbol
        self.cotacao = Par_moeda.func_cotacao()
        self.mm_menor
        self.mm_maior
        self.valor_minimo
        self.pares_possiveis

    def func_cotacao(self):
        ultima_transacao = client.get_recent_trades(symbol=moeda, limit=1)
        self.cotacao = float(ultima_transacao[-1]['price'])

    def calc_mm(self):

        for i, kline in enumerate(client.get_historical_klines_generator(moeda, Client.KLINE_INTERVAL_1MINUTE, limit=14)):
            ma14 += float(kline[4])
        self.mm_menor = ma14 / 14

        for i, kline in enumerate(client.get_historical_klines_generator(moeda, Client.KLINE_INTERVAL_1MINUTE, limit=36)):
            ma36 += float(kline[4])
        self.mm_maior = ma36 / 36
    
        
class Usuario():

    def __init__(self):
        self.moedas
        self.saldos
        self.trades
        self.orders
        self.posicao
