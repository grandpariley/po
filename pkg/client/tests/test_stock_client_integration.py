import unittest, pandas
from pkg.client.stock_client import StockClient


class StockClientTest(unittest.TestCase):
    @unittest.skip("enable to test finnhub; otherwise leave disabled so that we don't call out each time unit tests are run")
    def test_integration(self):
        stock_client = StockClient()
        data = stock_client.get_stock_data()
        print(pandas.DataFrame(data))