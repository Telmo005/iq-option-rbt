import numpy as np


class ConvertArrayCandles:

    def read(self, candles):
        inputs = {
            'open': np.array([]),
            'high': np.array([]),
            'low': np.array([]),
            'close': np.array([]),
            'volume': np.array([]),
            'from': np.array([]),
            'at': np.array([]),
            'to': np.array([])
        }

        for timestamp in list(candles):
            inputs["open"] = np.append(inputs["open"], candles[timestamp]["open"])
            inputs["high"] = np.append(inputs["high"], candles[timestamp]["max"])
            inputs["low"] = np.append(inputs["low"], candles[timestamp]["min"])
            inputs["close"] = np.append(inputs["close"], candles[timestamp]["close"])
            inputs["volume"] = np.append(inputs["volume"], candles[timestamp]["volume"])
            inputs["from"] = np.append(inputs["from"], candles[timestamp]["from"])
            inputs["at"] = np.append(inputs["at"], candles[timestamp]["at"])
            inputs["to"] = np.append(inputs["to"], candles[timestamp]["to"])
        return inputs

    pass


pass
