class Candle:
    open = ''
    high = ''
    low = ''
    close = ''
    volume = ''

    def __int__(self, arrayCandles):
        self.open = arrayCandles['close'][-1]
        self.high = arrayCandles['high'][-1]
        self.low = arrayCandles['low'][-1]
        self.close = arrayCandles['close'][-1]
        self.volume = arrayCandles['volume'][-1]

    pass
