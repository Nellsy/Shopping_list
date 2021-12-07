from cl_item import Item


class ShoppingList:

    def __init__(self, name):
        self.shop_list_name = name
        self.shop_list = []

    def set_add_item(self, stuff, qty_type, qty, market):
        new_item = Item(stuff, qty_type, qty, market)
        self.shop_list.append(new_item)

    def get_list_printed(self):
        for i in range(0, len(self.shop_list)):
            print(self.shop_list[i])

    def get_list_by_market(self, searched_market):
        list_by_market = []
        for i in self.shop_list:
            if i.market == searched_market:
                list_by_market.append(i)
        return list_by_market

    def print_list_by_market(self, searched_market):
        kyp = self.get_list_by_market(searched_market)
        for i in range(0, len(kyp)):
            print(kyp[i])


    # def __repr__(self):
    #     return self.shop_list_name

    # def get_list_by_input_shop(self):
