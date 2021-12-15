import unittest

from pkg.client.stock_client import default_stock_data


class StockClientTest(unittest.TestCase):
    def test_integration(self):
        data = default_stock_data()
        print(data)
        self.assertTrue(True)
