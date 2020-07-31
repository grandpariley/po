import os, finnhub, unittest

stocks = ['AAPL', 'MSFT', 'AMZN', 'TSLA', 'NVDA', 'GE', 'GOOGL', 'UA', 'XOM', 'NCLH']

class StockClient:
    def __init__(self):
        self.finnhub_client = finnhub.Client(api_key=os.getenv("FINNHUB_API_KEY"))
        self.stocks = {}

    def get_stock_data(self):
        if self.stocks:
            return self.stocks
        prices = []
        for stock in stocks:
            prices.append(self.finnhub_client.price_target(stock))
        self.stocks = self.format(prices)
        return self.stocks
