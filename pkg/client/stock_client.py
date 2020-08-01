import os
import finnhub
import unittest

stocks = ['AAPL', 'MSFT', 'AMZN', 'TSLA',
          'NVDA', 'GE', 'GOOGL', 'UA', 'XOM', 'NCLH']


class StockClient:
    def __init__(self):
        self.finnhub_client = finnhub.Client(
            api_key=os.getenv("FINNHUB_API_KEY"))
        self.stocks = {}

    def get_stock_data(self):
        if self.stocks:
            return self.stocks
        prices = []
        for stock in stocks:
            prices.append(self.finnhub_client.price_target(stock))
        self.stocks = format(prices)
        return self.stocks

    def format(self, data):
        return [
            {
                'price': self.get_price(d), 
                'risk': self.get_risk(d),
                'reward': self.get_reward(d)
            } for d in data
        ]
    
    def get_price(self, d):
        return 0.00
    
    def get_risk(self, d):
        return 0.00
    
    def get_reward(self, d):
        return 0.00