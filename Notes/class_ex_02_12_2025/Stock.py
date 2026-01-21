class Stock:
    def __init__(self, symbol, name, prevClosingPrice,
                 current_price):
        self.symbol = symbol
        self.name = name
        self.prevClosingPrice = prevClosingPrice
        self.current_price = current_price


    def getChangePercent(self):
        change = self.prevClosingPrice - self.current_price
        percentage = change / self.prevClosingPrice
        return str(percentage * 100)+"%"
