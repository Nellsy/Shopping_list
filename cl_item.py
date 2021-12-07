class Item:

    def __init__(self, stuff, qty_type, qty, market):
        self.item_name = stuff
        self.item_qty_type = qty_type
        self.item_qty = qty
        self.market = market
        self.item_is_bought = False

    def set_qty(self, qty):
        self.item_qty = qty

    # def set_item_status(self):
    #     self.item_status = status

    def __get_item_info(self):
        item_info = (self.item_name + " - " + str(self.item_qty) + " " + self.item_qty_type)
        return item_info

    def __repr__(self):
        return self.__get_item_info()