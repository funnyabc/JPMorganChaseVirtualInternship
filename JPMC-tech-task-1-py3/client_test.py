import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))
  
  def test_getDataPoint_calculatePriceBidEqualToAsk(self):
    quote = {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 121.2, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidLessThanAsk(self):
    quote = {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quote = {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'}
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  """ ------------ Add more unit tests ------------ """
  def test_getDataPoint_isTuple(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for quote in quotes:
      self.assertIsInstance(getDataPoint(quote), tuple)
  
  def test_getRatio_divide(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    
    for quote in quotes:
      self.assertAlmostEqual(getRatio(quote['top_ask']['price'], quote['top_bid']['price']), quote['top_ask']['price'] / quote['top_bid']['price'])
    
  def test_getRatio_divideByZero(self):
    price_a = 119.2
    price_b = 0
    self.assertFalse(getRatio(price_a, price_b))

  def test_getRatio_zeroAskPrice(self):
    price_a = 0
    price_b = 119.2
    self.assertEqual(getRatio(price_a, price_b), 0)

  def test_getRatio_samePrice(self):
    price_a = 119.2
    price_b = 119.2
    self.assertEqual(getRatio(price_a, price_b), 1)
  
  def test_getRatio_ratioGreaterThanOne(self):
    price_a = 122
    price_b = 119.2
    self.assertGreater(getRatio(price_a, price_b), 1)
  
  def test_getRatio_ratioLessThanOne(self):
    price_a = 119.2
    price_b = 122
    self.assertLess(getRatio(price_a, price_b), 1)

if __name__ == '__main__':
    unittest.main()
