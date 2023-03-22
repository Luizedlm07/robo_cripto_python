from class_usuario import client, Client



class Par_moeda():          ## Classe que armazena todos os dados referentes a moedas

    def __init__(self, symbol):
        self.symbol = symbol
        self.cotacao = 0
        self.mm_menor = 0
        self.mm_maior = 0
        self.lista_mm_menor = []
        self.lista_mm_maior = []
        
    def cotar(self, symbol):
        self.cotacao = client.get_recent_trades(symbol=symbol, limit=1)
        self.cotacao = float(self.cotacao[-1]['price'])

    def calculo_media_movel(self, symbol):
        self.mm_menor = 0
        for kline in client.get_historical_klines_generator(symbol, Client.KLINE_INTERVAL_1MINUTE, limit=25):
            self.mm_menor += float(kline[4])
        self.mm_menor /= 25

        self.mm_maior = 0
        for kline in client.get_historical_klines_generator(symbol, Client.KLINE_INTERVAL_1MINUTE, limit=99):
            self.mm_maior += float(kline[4])
        self.mm_maior /= 99
    
    def armazenar_medias_moveis(self):
        self.lista_mm_menor.append(self.mm_menor)
        self.lista_mm_maior.append(self.mm_maior)
    
    def atualizar_valores(self, symbol):
        self.cotar(symbol)
        self.calculo_media_movel(symbol)
        self.armazenar_medias_moveis()
