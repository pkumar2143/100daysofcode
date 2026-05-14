from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def ask_new_order():
    start_Q = input('Start a new order? y/[n]: ')
    if start_Q == 'y':
        print("\n"*10 + "Starting new order...!")
        return True
    else:
        print('Thanks for your business! Goodbye!')
        return False

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

new_order = True
while new_order:
    user_drink_item = input( f"Which drink do you want? ({menu.get_items()}): " )
    while user_drink_item not in ['latte', 'espresso', 'cappuccino','report']:
        user_drink_item = input( f"Which drink do you want? ({menu.get_items()}): " )


    if user_drink_item == 'report':
        coffee_maker.report()
    else:
        user_drink_item = menu.find_drink(order_name=user_drink_item)

        if coffee_maker.is_resource_sufficient(drink=user_drink_item):
            if money_machine.make_payment(cost=user_drink_item.cost):
                coffee_maker.make_coffee(order=user_drink_item)
            else:
                print('Insufficient funds. Money refunded')
        else:
            print('No resources!')

    new_order = ask_new_order()


