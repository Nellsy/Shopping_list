"""Class List makes possible creating (currently it's pre-defined) and printing the list with all it's items"""
from cl_item import Item


class ShoppingList:

    # constructor - it is a list with a name
    def __init__(self, name):
        self.shop_list_name = name
        self.shop_list = []

    # Let's add items in the list
    def set_add_item(self, stuff, qty_type, qty, market):
        new_item = Item(stuff, qty_type, qty, market)
        self.shop_list.append(new_item)

    # Let's print the list
    def get_list_printed(self):
        for i in range(0, len(self.shop_list)):
            print(self.shop_list[i])

    # Getter for a list by market
    def get_list_by_market(self, searched_market):
        list_by_market = []
        for i in self.shop_list:
            if i.market == searched_market:
                list_by_market.append(i)
        return list_by_market

    # Let's print the list by market (every code needs a Keep Your Promises for Good luck). Future - only give options
    # for markets that are planed for shopping
    def print_list_by_market(self, searched_market):
        kyp = self.get_list_by_market(searched_market)
        for i in range(0, len(kyp)):
            print(kyp[i])
