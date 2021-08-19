# Константа для ставки налога.
TAX_RATE = 0.05

# Класс ServiceQuote.
class ServiceQuote:
    def __init__(self, parts_charges, labor_charges):
        self.__parts_charges = parts_charges
        self.__labor_charges = labor_charges

    def set_parts_charges(self, parts_charges):
        self.__set_parts_charges = parts_charges

    def set_labor_charges(self, labor_charges):
        self.__labor_charges = labor_charges

    def get_parts_charges(self):
        return self.__get_parts_charges

    def get_labor_charges(self):
        return self.__labor_charges

    def get_sales_tax(self):
        return self.__get_sales_tax

    def get_total_charges(self):
        return self.__get_total_charges
