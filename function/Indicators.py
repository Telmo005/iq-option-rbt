from talib import EMA


class Indicators:
    def Ema(self, inputs, timeperiod):
        ema = EMA(inputs['close'], timeperiod)
        return ema


pass
