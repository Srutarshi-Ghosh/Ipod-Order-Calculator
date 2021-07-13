
from Exceptions.OutOfStockException import OutOfStockException

class Country:

    def __init__(self, name, price_per_ipod, ipods_in_stock=100, shipping_price_per_ten_units=400):
        self.name = name
        self.ipods_in_stock = ipods_in_stock
        self.price_per_ipod = price_per_ipod
        self.shipping_price_per_ten_units = shipping_price_per_ten_units


    def calculate_order_cost(self, number_of_ipods_ordered):
        if number_of_ipods_ordered > self.ipods_in_stock:
            raise OutOfStockException
        return number_of_ipods_ordered * self.price_per_ipod

    def calculate_shipping_order_cost(self, number_of_ipods_ordered):
        return self.calculate_order_cost(number_of_ipods_ordered) + ((number_of_ipods_ordered // 10) * self.shipping_price_per_ten_units)

