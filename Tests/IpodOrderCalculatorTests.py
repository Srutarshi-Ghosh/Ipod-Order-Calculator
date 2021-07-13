import unittest
from models.IpodOrderCalculator import IpodOrderCalculator
from Exceptions.OutOfStockException import OutOfStockException
from Exceptions.InvalidOrderSizeException import InvalidOrderSizeException
from Exceptions.InvalidCountryNameException import InvalidCountryNameException

class MyTestCase(unittest.TestCase):

    def test_should_give_correct_output_when_valid_order_is_placed(self):
        ipod_order_calculator = IpodOrderCalculator()
        ordering_country_name = "Brazil"
        ipods_ordered = 5
        correct_output = 500
        self.assertTrue(correct_output, ipod_order_calculator.get_order_cost(ordering_country_name, ipods_ordered))

    def test_should_raise_invalid_country_name_exception_when_invalid_country_name_is_passed(self):
        ipod_order_calculator = IpodOrderCalculator()
        ordering_country_name = "India"
        ipods_ordered = 50
        self.assertRaises(InvalidCountryNameException, ipod_order_calculator.get_order_cost, ordering_country_name, ipods_ordered)

    def test_should_raise_out_of_stock_exception_when_order_greater_than_stock_is_placed(self):
        ipod_order_calculator = IpodOrderCalculator()
        ordering_country_name = "Brazil"
        ipods_ordered = 250
        self.assertRaises(OutOfStockException, ipod_order_calculator.get_order_cost, ordering_country_name, ipods_ordered)

    def test_should_raise_invalid_order_size_exception_when_invalid_order_is_placed(self):
        ipod_order_calculator = IpodOrderCalculator()
        ordering_country_name = "Brazil"
        ipods_ordered = 123
        self.assertRaises(InvalidOrderSizeException, ipod_order_calculator.get_order_cost, ordering_country_name, ipods_ordered)





if __name__ == '__main__':
    unittest.main()
