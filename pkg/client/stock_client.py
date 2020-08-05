import os, finnhub

stock_names = ['AAPL', 'MSFT', 'TSLA',
          'NVDA', 'GOOGL']


class StockClient:
    def __init__(self):
        self.finnhub_client = finnhub.Client(
            api_key=os.getenv("FINNHUB_API_KEY"))
        self.stocks = [] if os.environ['EXTERNAL_API'] else self.default_stock_data()

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

    def default_stock_data(self):
        return {
            'AAPL': {
                'price': 370.81, 
                'risk': 254.57,
                'reward': 450 
            }, 
            'MSFT': {
                'price': 227.65, 
                'risk': 80,
                'reward': 260 
            }, 
            'TSLA': {
                'price': 1115.34, 
                'risk': 2521,
                'reward': 2608 
            },
            'NVDA': {
                'price': 406.18, 
                'risk': 240,
                'reward': 500 
            }, 
            'GOOGL': {
                'price': 1515.73, 
                'risk': 530,
                'reward': 1800 
            }
        }
