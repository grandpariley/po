import unittest, os
from pkg.client.stock_client import StockClient


class StockClientTest(unittest.TestCase):
    @unittest.skipIf(not bool(os.environ['RUN_EXTERNAL_API_TESTS']), "calls external api")
    def test_integration(self):
        stock_client = StockClient()
        data = stock_client.get_stock_data()
        print(data)