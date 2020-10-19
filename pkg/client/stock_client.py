import os, finnhub

stock_names = ['AAPL', 'MSFT', 'TSLA',
               'NVDA', 'GOOGL']


def default_stock_data():
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


def get_reward(d):
    return d['targetHigh']


def get_risk(d):
    return d['targetHigh'] - d['targetLow']


def get_price(d):
    return d['targetMean']


def format(data):
    return {
        d['symbol']: {
            'price': get_price(d),
            'risk': get_risk(d),
            'reward': get_reward(d)
        } for d in data
    }


class StockClient:
    def __init__(self):
        self.finnhub_client = finnhub.Client(api_key=os.getenv("FINNHUB_API_KEY"))
        self.stocks = [] if os.getenv("EXTERNAL_API") else default_stock_data()

    def get_stock_data(self):
        if bool(self.stocks):
            return self.stocks
        prices = []
        for stock in stock_names:
            prices.append(self.finnhub_client.price_target(stock))
        self.stocks = format(prices)
        return self.stocks
