
def cotacao(moeda):
    from main import client, Client


    ultima_transacao = client.get_recent_trades(symbol=moeda, limit=1)
    valor_atual = float(ultima_transacao[-1]['price'])

    print(moeda, ': ', valor_atual, '\n')

    ma14 = 0
    ma36 = 0

    for i, kline in enumerate(client.get_historical_klines_generator(moeda, Client.KLINE_INTERVAL_1MINUTE, limit=14)):
        ma14 += float(kline[4])
    ma14 /= 14

    print(f"Moving Average(14): {ma14}")

    for i, kline in enumerate(client.get_historical_klines_generator(moeda, Client.KLINE_INTERVAL_1MINUTE, limit=36)):
        ma36 += float(kline[4])
    ma36 /= 36

    print(f"Moving Average(36): {ma36}\n")

    return ma14, ma36, valor_atual
     