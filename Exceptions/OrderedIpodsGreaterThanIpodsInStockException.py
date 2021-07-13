

class OrderedIpodsGreaterThanIpodsInStockException(Exception):

    def __str__(self):
        return "Number of Ordered Ipods are greater than Ipods present in the Stock"