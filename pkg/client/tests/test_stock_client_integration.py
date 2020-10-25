import unittest
from pkg.client.stock_client import StockClient
from pkg.consts import Constants


class StockClientTest(unittest.TestCase):
    @unittest.skipIf(not Constants.EXTERNAL_API, "calls external api")
    def test_integration(self):
        stock_client = StockClient()
        data = stock_client.get_stock_data()
        print(data)
