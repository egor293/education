# Ваш API-ключ и секрет с Binance
apikey = 'yourapikey'
apisecret = 'your_api_secret'

client = Client(api_key, api_secret)

# Получаем исторические данные
def get_data(symbol, interval, lookback):
    frame = pd.DataFrame(client.get_historical_klines(symbol, interval, lookback))
    frame = frame.iloc[:, :6]
    frame.columns = ['time', 'open', 'high', 'low', 'close', 'volume']
    frame = frame.set_index('time')
    frame.index = pd.to_datetime(frame.index, unit='ms')
    frame = frame.astype(float)
    return frame

# Стратегия на основе индикатора RSI
def strategy(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['close'], window=14).rsi()

    # Условия покупки и продажи
    df['buy_signal'] = (df['rsi'] < 30)
    df['sell_signal'] = (df['rsi'] > 70)

    return df

# Основной цикл бота
def bot():
    while True:
        df = get_data('ETHUSDT', '1h', '2 days ago UTC')
        df = strategy(df)

        last_row = df.iloc[-1]

        if last_row['buy_signal']:
            print("Сигнал на покупку")
            # Здесь можно разместить ордер на покупку

        if last_row['sell_signal']:
            print("Сигнал на продажу")
            # Здесь можно разместить ордер на продажу

        time.sleep(3600)  # Бот обновляется каждый час

if name == "main":
    bot()