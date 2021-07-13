
class OutOfStockException(Exception):

    def __str__(self):
        return "Sorry we are out of stock"