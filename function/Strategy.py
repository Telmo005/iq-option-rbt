import time

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

        #balance_type = "TOURNAMENT"
        balance_type = "PRACTICE"
        #balance_type = "REAL"
        self.Iq.change_balance(balance_type)

        while True:
            try:
                candles = self.Iq.get_realtime_candles(self.goal, self.size)
                arrayCandles = ConvertArrayCandles().read(candles)

                # balance = self.Iq.get_balance()
                # if balance < 1000:
                #     shutdown_command = "shutdown /s /f /t 0"
                #     os.system(shutdown_command)
                #

                if arrayCandles['high'][-2] > arrayCandles['high'][-3]:
                    if arrayCandles['close'][-1] <= arrayCandles['open'][-1]:
                        operation = Operation(self.Iq, self.goal, self.amount, self.duration)
                        operation.action('call', self.size, arrayCandles['close'][-1])

                if arrayCandles['low'][-2] < arrayCandles['low'][-3]:
                    if arrayCandles['close'][-1] >= arrayCandles['open'][-1]:
                        operation = Operation(self.Iq, self.goal, self.amount, self.duration)
                        operation.action('put', self.size, arrayCandles['close'][-1])

            except:
                print("An exception occurred")

            # break
