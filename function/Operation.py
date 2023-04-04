class Operation:

    def __init__(self, Iq, actives, amount, duration):
        self.Iq = Iq
        self.actives = actives
        self.amount = amount
        self.duration = duration

    def action(self, action, size, price):
        print(self.actives)
        self.Iq.subscribe_strike_list(self.actives, self.duration)
        _, id = (self.Iq.buy_digital_spot(self.actives, self.amount, action, self.duration))

        print("Start operation: ", id)
        if id != "error":
            while True:
                check, win = self.Iq.check_win_digital_v2(id)
                if check == True:
                    break
            if win < 0:
                print("you loss " + str(win) + "$")
            else:
                print("you win " + str(win) + "$")
        else:
            print("please try again")


pass
