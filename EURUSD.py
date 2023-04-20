from iqoptionapi.stable_api import IQ_Option

from function.Strategy import Strategy


def connectIqOption():
    print("login...")
    Iq = IQ_Option("telmo.sigauquejr@gmail.com", "telmo005")
    Iq.connect()  # connect to iqoption
    print("connected ...")
    return Iq


Iq = connectIqOption()
CURRENCY = 'EURUSD'
candle1min = Strategy(Iq, CURRENCY, 1, 500, 1000, 1).readData()
