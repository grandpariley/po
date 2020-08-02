import os
import finnhub
import unittest

stock_names = ['AAPL', 'MSFT', 'AMZN', 'TSLA',
          'NVDA', 'GE', 'GOOGL', 'UA', 'XOM', 'NCLH']


class StockClient:
    def __init__(self):
        self.finnhub_client = finnhub.Client(
            api_key=os.getenv("FINNHUB_API_KEY"))
        self.stocks = []

    def get_stock_data(self):
        if bool(self.stocks):
            return self.stocks
        prices = []
        for stock in stock_names:
            prices.append(self.finnhub_client.price_target(stock))
        self.stocks = self.format(prices)
        return self.stocks

    def format(self, data):
        return {
            d['symbol']: {
                'price': self.get_price(d), 
                'risk': self.get_risk(d),
                'reward': self.get_reward(d)
            } for d in data
        }
    
    def get_price(self, d):
        return d['targetMean']
    
    def get_risk(self, d):
        return d['targetHigh'] - d['targetLow']
    
    def get_reward(self, d):
        return d['targetHigh']