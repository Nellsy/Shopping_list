class Item:

    def __init__(self, stuff, qty_type, qty, shop):
        self.item_name = stuff
        self.item_qty_type = qty_type
        self.item_qty = qty
        self.preferred_shop = shop
        self.item_is_bought = False

    def set_qty(self, qty):
        self.item_qty = qty

    def set_item_status(self):
        self.item_status = status

    def __repr__(self):
        return self.item_name


class ShoppingList:

    def __init__(self, name):
        self.shop_list_name = name
        self.shop_list = []

    def add_item(self, stuff, qty_type, qty, shop):
        new_item = Item(stuff, qty_type, qty, shop)
        self.shop_list.append(new_item)

    def __repr__(self):
        return self.shop_list_name

    # def __repr__(self):
    #     return self.shop_list


input_list_name = input("Name your list, sir: ")

my_list = ShoppingList(input_list_name)
# lidl_list.shop_list_name = "lidl_list"
my_list.add_item("flour", "pack", 1, "Lidl")
my_list.add_item("salmon", "piece", 2, "Metro")
my_list.add_item("coconut sugar", "pack", 1, "Metro")

print(my_list)
print(my_list.shop_list)

