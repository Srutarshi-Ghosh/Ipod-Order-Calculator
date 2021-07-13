import unittest
from models.Country import Country
from Exceptions.OutOfStockException import OutOfStockException


class CountryTest(unittest.TestCase):

    def test_should_return_order_cost_when_valid_order_is_placed(self):
        argentina = Country('Argentina', 50, 100)
        number_of_ipods = 50
        correct_output = 50 * number_of_ipods
        self.assertEqual(correct_output, argentina.calculate_order_cost(number_of_ipods))

    def test_should_throw_exception_when_invalid_order_is_placed(self):
        argentina = Country('Argentina', 50, 100)
        number_of_ipods = 120
        self.assertRaises(OutOfStockException, argentina.calculate_order_cost, number_of_ipods)

if __name__ == '__main__':
    unittest.main()
