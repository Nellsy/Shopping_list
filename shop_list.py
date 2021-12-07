from cl_list import ShoppingList


def muggle_exception():
    print("Mr Muggle, read the instructions carefully, please!\r\n")


def spine(option_list):
    print("\r\nSelect option:")
    for i in range(0, len(option_list)):
        print(f"{i+1} - {option_list[i]}")

    option_input = int(input("Answer: "))  # question for option

    if option_input == 1:
        new_item_loop()
    elif option_input == 2:
        if len(my_list.shop_list) == 0:
            print("You don't have any added items.\r\n")
            spine(options)
        else:
            my_list.get_list_printed()
            spine(options)
    elif option_input == 3:
        pick_market(markets)
        spine(options)
    elif option_input == 4:
        print("Good buy!")
        exit()
    else:
        muggle_exception()
        spine(option_list)


def get_markets(market_list, item_name):
    print(f"\r\nFrom where would you like to buy {item_name}?")
    for i in range(0, len(market_list)):
        print(f"{i+1} - {market_list[i]}")
    market_input = int(input("Choose the number of the shop: "))
    if market_input in range(1, (len(market_list)+1)):
        pass
    else:
        muggle_exception()
        get_markets(market_list, item_name)
    return market_input

def pick_market(market_list):
    print("Select shop to view list: ")
    for i in range(0, len(market_list)):
        print(f"{i+1} - {market_list[i]}")
    market_input = int(input("Choose the number of the shop: "))
    if market_input in range(1, (len(market_list)+1)):
        print(f"\r\n{markets[market_input-1]}")
        my_list.print_list_by_market(markets[market_input-1])
    else:
        muggle_exception()
        pick_market(market_list)


def new_item_question():
    print("""\r\nWould you like to add another item?
1 - yes
0 - no""")
    i = int(input("Answer: "))
    if i == 1:
        new_item_loop()
    elif i == 0:
        spine(options)
    else:
        muggle_exception()
        new_item_question()


def new_item_loop():
        print(f"\r\nNew item")
        product = input("- product name: ")
        unit = input("- unit: ")
        quantity = input("- qty: ")

        market_input = get_markets(markets, product)  # question for shop, see the def

        my_list.set_add_item(product, unit, quantity, markets[market_input - 1])

        new_item_question()

input_list_name = "Shopping List"
my_list = ShoppingList(input_list_name)

# list of options - pre-defined
options = ["Add new item", "Print shopping list", "Print shopping list by shop", "Exit"]

# list of markets - pre-defined
markets = ["Metro", "Lidl", "Kaufland", "Fantastiko", "Marketplace - Mladost", "Marketplace - Krasno selo"]

print("Welcome to ShoppingList app")

spine(options)
