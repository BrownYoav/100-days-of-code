from coffee_data import *


def report(dict_resources: dict) -> str:
    water = dict_resources['water']
    milk = dict_resources['milk']
    coffee = dict_resources['coffee']
    money = dict_resources['money']
    return f'Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}'


def check_resources(dict_resources: dict, dict_menu: dict, coffee_name: str) -> bool:
    resource_water = dict_resources['water']
    resource_milk = dict_resources['milk']
    resource_coffee = dict_resources['coffee']
    drink_water = dict_menu[coffee_name]['ingredients']['water']
    drink_milk = dict_menu[coffee_name]['ingredients']['milk']
    drink_coffee = dict_menu[coffee_name]['ingredients']['coffee']
    enough_resources = True
    if resource_coffee < drink_coffee:
        print('Sorry there is not enough coffee.')
        enough_resources = False
    if resource_milk < drink_milk:
        print('Sorry there is not enough milk.')
        enough_resources = False
    if resource_water < drink_water:
        print('Sorry there is not enough water.')
        enough_resources = False
    return enough_resources


coffee1 = {
    "ingredients": {
        "water": 50,
        "milk": 0,
        "coffee": 18,
    },
    "cost": 1.5,
}


def process_coins(quarters_amount: int, dimes_amount: int, nickles_amount: int, pennies_amount: int, dict_menu: dict,
                  coffee_name: str) -> bool:
    money_inserted = quarters_amount * 0.25 + dimes_amount * 0.1 + nickles_amount * 0.05 + pennies_amount * 0.01
    drink_cost = dict_menu[coffee_name]['cost']
    change = round(money_inserted - drink_cost, 2)

    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f'Here is ${change} in change.')
        return True


def make_coffee(dict_resources: dict, dict_menu: dict, coffee_name: str) -> str:
    """receives coffe and resources than minuses the resources, adds cost of coffe to resources, output coffe prompt"""
    drink_water = dict_menu[coffee_name]['ingredients']['water']
    drink_milk = dict_menu[coffee_name]['ingredients']['milk']
    drink_coffee = dict_menu[coffee_name]['ingredients']['coffee']
    drink_cost = dict_menu[coffee_name]['cost']

    # subtracts resources and adds cost to machine
    dict_resources['money'] += drink_cost
    for item in MENU[coffee_name]['ingredients']:
        dict_resources[item] -= MENU[coffee_name]['ingredients'][item]

    # returns output
    return f'Here is your {coffee_name} ☕️. Enjoy!'


# print(report(resources))
# print(check_resources(resources, coffee1))
# process_coins(4,4,1,1,MENU,'espresso')
# make_coffee(resources,MENU,'espresso')
# print(report(resources))
#

# print(type(coffee1))
# print(coffee1['ingredients'])
def coffee_machine():
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'report':
        print(report(resources))
    elif user_choice == 'off':
        return
    elif user_choice == 'cappuccino' or user_choice == 'latte' or user_choice == 'espresso':
        if check_resources(resources, MENU, user_choice):
            print('Please insert coins.')
            quarters = int(input('how many quarters?: '))
            dimes = int(input('how many dimes?: '))
            nickels = int(input('how many nickels?: '))
            pennies = int(input('how many pennies?: '))
            if process_coins(quarters, dimes, nickels, pennies, MENU, user_choice):
                print(make_coffee(resources, MENU, user_choice))
    else:
        print("sorry I didn't get that please type again")
    coffee_machine()


print(logo)
coffee_machine()
