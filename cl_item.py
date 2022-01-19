"""Class Item makes defining every item possible"""


class Item:

    # Constructor
    def __init__(self, stuff, qty_type, qty, market):
        self.item_name = stuff
        self.item_qty_type = qty_type
        self.item_qty = qty
        self.market = market

    # Getter for the Item
    def __get_item_info(self):
        item_info = (self.item_name + " - " + str(self.item_qty) + " " + self.item_qty_type + " from " + self.market)
        return item_info

    def __repr__(self):
        return self.__get_item_info()
