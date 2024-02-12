from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
machine = CoffeeMaker()
menu = Menu()
print(menu.find_drink('latte').ingredients)
is_on = True

#
while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino): ")
    drink = menu.find_drink(choice)
    if choice == "off":
        is_on = False
    elif choice == "report":
        machine.report()
    else:
        if machine.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                machine.make_coffee(drink)
