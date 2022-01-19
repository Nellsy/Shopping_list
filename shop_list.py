"""The application offers a possibility to track your shopping list. You are able to write down everything that is
needed from the shops around by the item, it's unit (pc, kg, l, pack) and the preferred shop. After that there are
options to check the whole list or to see only the items that are marked for buying from the shop you are headed to."""

# Import the List class, the Item class is called in it so there is no need to call it, too
from cl_list import ShoppingList


# Kindly ask the user to read the instructions again - call that function for every wrong enter
def muggle_exception():
    print("Mr Muggle, read the instructions carefully, please!\r\n")


#  The main menu of the app
def spine(option_list):
    print("\r\nSelect option:")
    for i in range(0, len(option_list)):
        print(f"{i + 1} - {option_list[i]}")

    option_input = input("Answer: ")

    try:
        option_input = int(option_input)
        pass
    except ValueError:
        muggle_exception()
        spine(option_list)

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


# choosing the shop from which to buy item
def get_markets(market_list, item_name):
    print(f"\r\nFrom where would you like to buy {item_name}?")
    for i in range(0, len(market_list)):
        print(f"{i + 1} - {market_list[i]}")

    market_input = input("Choose the number of the shop: ")

    if market_input.isnumeric():
        market_input = int(market_input)
        if market_input in range(1, (len(market_list) + 1)):
            pass
        else:
            print("down")
            muggle_exception()
            return get_markets(market_list, item_name)
    else:
        print("down down")
        muggle_exception()
        return get_markets(market_list, item_name)

    return market_input


# choosing the shop for which to show list
def pick_market(market_list):
    print("Select shop to view list: ")
    for i in range(0, len(market_list)):
        print(f"{i + 1} - {market_list[i]}")

    market_input = input("Choose the number of the shop: ")

    if market_input.isnumeric():
        market_input = int(market_input)
        if market_input in range(1, (len(market_list) + 1)):
            print(f"\r\n{markets[market_input - 1]}")
            my_list.print_list_by_market(markets[market_input - 1])
        else:
            muggle_exception()
            pick_market(market_list)
    else:
        muggle_exception()
        pick_market(market_list)


# Does the user need to add another item?
def new_item_question():
    print("""\r\nWould you like to add another item?
1 - yes
0 - no""")
    i = input("Answer: ")
    if i.isnumeric():
        i = int(i)
        if i == 1:
            new_item_loop()
        elif i == 0:
            spine(options)
        else:
            muggle_exception()
            new_item_question()
    else:
        muggle_exception()
        new_item_question()


# When the User needs to add another item
def new_item_loop():
    print(f"\r\nNew item")
    product = input("- product name: ")
    unit = input("- unit: ")
    quantity = input("- qty: ")

    market_input = get_markets(markets, product)  # question for shop, see the def

    my_list.set_add_item(product, unit, quantity, markets[market_input - 1])

    new_item_question()


# Pre-set shopping list. Future feature - to be able to create different lists (for dinner, for camping...)
input_list_name = "Shopping List"
my_list = ShoppingList(input_list_name)

# list of options - pre-defined. Future feature - to change or delete an item
options = ["Add new item", "Print shopping list", "Print shopping list by shop", "Exit"]

# list of markets - pre-defined. We can't expect the user to write them down every time. Future - to be able to
# add another market that is not a regular for a specific list (sports, furniture)
markets = ["Metro", "Lidl", "Kaufland", "Fantastiko", "Marketplace - Mladost", "Marketplace - Krasno selo"]

# Say Hi! to the User
print("Welcome to ShoppingList app")

# Let the magic happen
spine(options)
