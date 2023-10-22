import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {
                "top_ask": {"price": 121.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """
        results = []

        expected_result = [
            [
                quotes[i]["stock"],
                quotes[i]["top_bid"]["price"],
                quotes[i]["top_ask"]["price"],
                (quotes[i]["top_ask"]["price"] + quotes[i]["top_bid"]["price"]) / 2,
            ]
            for i in range(len(quotes))
        ]
        for quote in quotes:
            results.append([*getDataPoint(quote=quote)])

        self.assertEqual(results, expected_result)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {
                "top_ask": {"price": 119.2, "size": 36},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 120.48, "size": 109},
                "id": "0.109974697771",
                "stock": "ABC",
            },
            {
                "top_ask": {"price": 121.68, "size": 4},
                "timestamp": "2019-02-11 22:06:30.572453",
                "top_bid": {"price": 117.87, "size": 81},
                "id": "0.109974697771",
                "stock": "DEF",
            },
        ]
        """ ------------ Add the assertion below ------------ """

        results = []

        expected_result = [
            [
                quotes[i]["stock"],
                quotes[i]["top_bid"]["price"],
                quotes[i]["top_ask"]["price"],
                (quotes[i]["top_ask"]["price"] + quotes[i]["top_bid"]["price"]) / 2,
            ]
            for i in range(len(quotes))
        ]
        for quote in quotes:
            results.append([*getDataPoint(quote=quote)])

        self.assertEqual(results, expected_result)

    """ ------------ Add more unit tests ------------ """


class ClientTest(unittest.TestCase):
    def test_getRatio_happy_path(self):
        prices = [(121.2, 120.48), (121.68, 117.87)]

        results = []
        expected_result = [[price[0] / price[-1]] for price in prices]
        for price in prices:
            results.append([getRatio(price_a=price[0], price_b=price[-1])])

        self.assertEqual(results, expected_result)

    def test_getRatio_sad_path(self):
        prices = [(121.2, 0), (121.68, 0)]

        results = []
        expected_result = [[None], [None]]
        for price in prices:
            results.append([getRatio(price_a=price[0], price_b=price[-1])])

        self.assertEqual(results, expected_result)


if __name__ == "__main__":
    unittest.main()
