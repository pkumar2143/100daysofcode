# Coffee Machine Project
# Coin operated: no pennies
# Other requirements:
#   + Entering 'report' gives summary of coffee machine resources
#   + We enter the amount of each coin type individually.
#   + Machine gives change.
#   + Entering 'report' after ordering, should reduce the resources.
#   + Gives notes if there are insufficient resources.
#   + If not enough money provided, refund, and asks again.

def menu_choice_clean(user_input):
    '''
    Reducing need for user effort by allowing them to enter either the full menu item name or just the first letter.
    (Later, try implementing autofill...)
    '''
    if (user_input == 'espresso') or (user_input == 'e'):
        return 'espresso'
    elif (user_input == 'latte') or (user_input == 'l'):
        return 'latte'
    elif (user_input == 'cappuccino') or (user_input == 'c'):
        return 'cappuccino'
    elif (user_input == 'report') or (user_input == 'r'):
        return 'report'
    else:
        return None

def coin_entry(coin_type):
    '''
    Check whether user is entering a legitimate number of coins (e.g. not 3.5 nickels, etc.)
    '''
    coin_fulfilled_Q = False
    while not coin_fulfilled_Q:
        try:
            return int(input(f'How many {coin_type}? : ')) # if successful, simply returns
        except:
            print('Invalid entry') # if not successful, keeps boolean false and repeats.
            continue

def coin_total():
    quarters = coin_entry('quarters')
    dimes    = coin_entry('dimes')
    nickels  = coin_entry('nickels')

    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05
    
def machine_report(resources):
    full_report = "\n>>>> Coffee Machine Resources\n" + \
                f"\n     Water = {resources['water']}" + \
                f"\n     Milk = {resources['milk']}" + \
                f"\n     Coffee = {resources['coffee']}\n"
    #print(full_report)
    return full_report

def check_resource(user_menu_item, resources, user_money):
    if  ( (resources['water']  - menu[user_menu_item]['water'] ) < 0 ) or ( (resources['milk']   - menu[user_menu_item]['milk']) < 0 ) or \
        ( (resources['coffee'] - menu[user_menu_item]['coffee']) < 0 ):
        return False
    else:
        return True

def coffee_main_processor(user_choice_clean):
    '''
    Manages all coffe processing.
    '''
    menu_item = user_choice_clean

    if menu_item == 'report':
        machine_report(resources=resources)
    else:
        menu_item_price = menu[menu_item]['cost']
        print(f'{menu_item.capitalize()} Price = {menu_item_price:.2f}')
        
        full_total = coin_total()
        print(f'You inserted: ${full_total:.2f}')

        if full_total < menu_item_price:
            #print(f"Not enough funds. Here's your refund: ${full_total:.2f}")
            return f"Not enough funds. Here's your refund: ${full_total:.2f}"
        else:
            print(f"Your change is ${-(menu_item_price - full_total):.2f}")
            resources['money']  += menu_item_price
            if check_resource(menu_item, resources, full_total):
                resources['water']  -= menu[menu_item]['water']
                resources['milk']   -= menu[menu_item]['milk']
                resources['coffee'] -= menu[menu_item]['coffee']

                return f"Here's your Coffee: {menu_item}"
            else: 
                print(f"Not enough resources!")
                print(f"Here's the current resources: \n{machine_report(resources)}")
                print(f"Here's your_refund: \n{full_total:.2f}")
                return 'Low Resources'




print('\n'*10+'++++++++++++++++++++++ Welcome to the Coffee Machine ++++++++++++++++++++++')

menu = {
    'espresso':   {'water':50,   'coffee': 18, 'milk': 0,   'cost': 1.50},
    'latte':      {'water':200,  'coffee': 24, 'milk': 150, 'cost': 2.50},
    'cappuccino': {'water': 250, 'coffee': 24, 'milk': 100, 'cost': 3.00}
}

resources = {
    'water':  300,
    'milk':   200,
    'coffee': 100,
    'money':  0
}

new_order = True
while new_order:

    user_input = input('Enter your menu item; [e]spresso/[l]atte/[c]appuccino : ').lower()
    user_input = menu_choice_clean(user_input)

    while not ( ( user_input == 'espresso' ) or ( user_input == 'latte' )  or ( user_input == 'cappuccino' ) or ( user_input == 'report') ):
        user_input = input('Enter your menu item; [e]spresso/[l]atte/[c]appuccino : ').lower()
        user_input = menu_choice_clean(user_input)

    #print(f'User Entry = {user_input}')

    print(coffee_main_processor(user_choice_clean=user_input))

    order_again_ask = input('Would you like to start a new order? y/[n]: ')
    if order_again_ask != 'y':
        print('Thanks for your time! Goodbye!')
        new_order = False
        break
    else: 
        continue





