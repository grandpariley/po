import unittest
from pkg.client.stock_client import StockClient


class StockClientTest(unittest.TestCase):
    @unittest.skip("calls external api")
    def test_integration(self):
        stock_client = StockClient()
        data = stock_client.get_stock_data()
        print(data)