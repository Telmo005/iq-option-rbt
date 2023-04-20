import time

from talib import RSI

from function.ConvertArrayCandles import ConvertArrayCandles
from function.Operation import Operation


class Strategy:

    def __init__(self, Iq, goal, size, maxdict, amount, duration):
        self.Iq = Iq
        self.goal = goal
        self.size = size
        self.maxdict = maxdict

        self.amount = amount
        self.duration = duration

    def readData(self):
        print("start stream...goal: ", self.goal, 'time: ', self.size, ' maxdict: ', self.maxdict)
        self.Iq.start_candles_stream(self.goal, self.size, self.maxdict)
        alarme = 'alerts/alert1.wav'

        while True:
            try:
                candles = self.Iq.get_realtime_candles(self.goal, self.size)
                arrayCandles = ConvertArrayCandles().read(candles)
                closeRsi = RSI(arrayCandles['close'], timeperiod=14)
                print(closeRsi[-1])

                if closeRsi[-1] > 85:
                    operation = Operation(self.Iq, self.goal, self.amount, self.duration)
                    operation.action('put', self.size, arrayCandles['close'][-1])

                if closeRsi[-1] < 18:
                    operation = Operation(self.Iq, self.goal, self.amount, self.duration)
                    operation.action('call', self.size, arrayCandles['close'][-1])

                time.sleep(1)

            except:
                print('Ocorreu algum erro durante a interacao')
