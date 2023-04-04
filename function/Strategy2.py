from datetime import time

from talib import SMA

from function.ConvertArrayCandles import ConvertArrayCandles
from function.Operation import Operation


class Strategy2:

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

        # balance_type = "TOURNAMENT"
        balance_type = "PRACTICE"
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
                win = 0
                lose = 0
                money = 10000
                for i in range(1, 60):
                    if arrayCandles['high'][-i - 1] > arrayCandles['high'][-i - 2]:
                        if arrayCandles['close'][-i] > arrayCandles['open'][-i]:
                            win += 1
                            money += 892.07
                        else:
                            lose += 1
                            money -= 1000

                    if arrayCandles['low'][-i - 1] < arrayCandles['low'][-i - 2]:
                        if arrayCandles['close'][-i] < arrayCandles['open'][-i]:
                            win += 1
                            money += 892.07
                        else:
                            lose += 1
                            money -= 892.07

                print('win: ', win, 'lose: ', lose, 'money: ', money)
                # if arrayCandles['high'][-2] > arrayCandles['high'][-3]:
                #     if arrayCandles['close'][-1] <= arrayCandles['open'][-1]:
                #         operation = Operation(self.Iq, self.goal, self.amount, self.duration)
                #         operation.action('call', self.size, arrayCandles['close'][-1])
                #
                # if arrayCandles['low'][-2] < arrayCandles['low'][-3]:
                #     if arrayCandles['close'][-1] >= arrayCandles['open'][-1]:
                #         operation = Operation(self.Iq, self.goal, self.amount, self.duration)
                #         operation.action('put', self.size, arrayCandles['close'][-1])

                time.sleep(1)

            except:
                print("An exception occurred")

            break
