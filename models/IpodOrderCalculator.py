
from models.Country import Country
from Exceptions.InvalidOrderSizeException import InvalidOrderSizeException
from Exceptions.InvalidCountryNameException import InvalidCountryNameException
from Exceptions.OutOfStockException import OutOfStockException

class IpodOrderCalculator:

    def __init__(self):
        self.brazil = Country("Brazil", 100, 100)
        self.argentina = Country("Argentina", 50, 100)
        self.shipping_cost_per_ten_units = 400
        self.ipods_in_stock_per_country = 100


    def _get_ordering_and_shipping_country(self, country):
        if country == self.brazil.name:
            return self.brazil, self.argentina

        if country == self.argentina.name:
            return self.argentina, self.brazil

        raise InvalidCountryNameException

    @staticmethod
    def _check_valid_order_size(ordered_ipods):
        return ordered_ipods < 10 or ordered_ipods % 10 == 0

    @staticmethod
    def _calculate_shipping_country_cost(shipping_country, shipped_ipods):
        return shipping_country.calculate_shipping_order_cost(shipped_ipods)

    @staticmethod
    def _calculate_ordering_country_cost(ordering_country, shipped_ipods):
        return ordering_country.calculate_order_cost(shipped_ipods)

    def _calculate_minimum_cost_of_ordering(self, ordering_country, shipping_country, ordered_ipods):
        if ordered_ipods > self.ipods_in_stock_per_country:
            extra_ipods = ordered_ipods - self.ipods_in_stock_per_country
            order_price = min(self._calculate_ordering_country_cost(ordering_country, self.ipods_in_stock_per_country) + self._calculate_shipping_country_cost(shipping_country, extra_ipods),
                              self._calculate_ordering_country_cost(ordering_country, extra_ipods) + self._calculate_shipping_country_cost(shipping_country, self.ipods_in_stock_per_country))
            return order_price
        
        return min(self._calculate_ordering_country_cost(ordering_country, ordered_ipods), self._calculate_shipping_country_cost(shipping_country, ordered_ipods))

    def _check_country_stock(self, ordered_ipods):
        return ordered_ipods < (self.argentina.ipods_in_stock + self.brazil.ipods_in_stock)

    def get_order_cost(self, ordering_country_name, ordered_ipods):
        if not self._check_valid_order_size(ordered_ipods):
            raise InvalidOrderSizeException

        if not self._check_country_stock(ordered_ipods):
            raise OutOfStockException

        ordering_country, shipping_country = self._get_ordering_and_shipping_country(ordering_country_name)
        return self._calculate_minimum_cost_of_ordering(ordering_country, shipping_country, ordered_ipods)
        

        

if __name__ == '__main__':
    ipod_order_calculator = IpodOrderCalculator()
    # print(ipod_order_calculator.get_order_cost('Brazil', 5))
    print(ipod_order_calculator.get_order_cost('Brazil', 50))



