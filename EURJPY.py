from iqoptionapi.stable_api import IQ_Option

from function.Strategy import Strategy
from function.Strategy2 import Strategy2


def connectIqOption():
    print("login...")
    Iq = IQ_Option("telmo.sigauquejr@gmail.com", "telmo005")
    Iq.connect()  # connect to iqoption
    print("connected ...")
    return Iq


Iq = connectIqOption()
CURRENCY = 'EURJPY-OTC'
strategy = Strategy(Iq, CURRENCY, 60, 500, 1000, 1).readData()
