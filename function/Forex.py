from iqoptionapi.stable_api import IQ_Option

Iq = IQ_Option("telmo.sigauquejr@gmail.com", "telmo005")
Iq.connect()  # connect to iqoption
instrument_type = "forex"
instrument_id = "EURUSD"
side = "buy"  # input:"buy"/"sell"
amount = 327.11  # input how many Amount you want to play

# "leverage"="Multiplier"
leverage = 1.500  # you can get more information in get_available_leverages()

type = "limit"  # input:"market"/"limit"/"stop"

# for type="limit"/"stop"

# only working by set type="limit"
limit_price = None  # input:None/value(float/int)

# only working by set type="stop"
stop_price = None  # input:None/value(float/int)

# "percent"=Profit Percentage
# "price"=Asset Price
# "diff"=Profit in Money

stop_lose_kind = "percent"  # input:None/"price"/"diff"/"percent"
stop_lose_value = 95  # input:None/value(float/int)

take_profit_kind = None  # input:None/"price"/"diff"/"percent"
take_profit_value = None  # input:None/value(float/int)

# "use_trail_stop"="Trailing Stop"
use_trail_stop = True  # True/False

# "auto_margin_call"="Use Balance to Keep Position Open"
auto_margin_call = False  # True/False
# if you want "take_profit_kind"&
#            "take_profit_value"&
#            "stop_lose_kind"&
#            "stop_lose_value" all being "Not Set","auto_margin_call" need to set:True

use_token_for_commission = False  # True/False

check, order_id = Iq.buy_order(instrument_type=instrument_type, instrument_id=instrument_id,
                               side=side, amount=amount, leverage=leverage,
                               type=type, limit_price=limit_price, stop_price=stop_price,
                               stop_lose_value=stop_lose_value, stop_lose_kind=stop_lose_kind,
                               take_profit_value=take_profit_value, take_profit_kind=take_profit_kind,
                               use_trail_stop=use_trail_stop, auto_margin_call=auto_margin_call,
                               use_token_for_commission=use_token_for_commission)
print(Iq.get_order(order_id))
# print(Iq.get_positions("crypto"))
# print(Iq.get_position_history("crypto"))
# print(Iq.get_available_leverages("crypto", "BTCUSD"))
# print(Iq.close_position(order_id))
# print(Iq.get_overnight_fee("crypto", "BTCUSD"))
