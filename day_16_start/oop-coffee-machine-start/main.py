from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

make_coffee = CoffeeMaker()
coffee_menu = Menu()
money_transfer = MoneyMachine()

machine_on = True
while machine_on:
    choices = coffee_menu.get_items()
    coffee_type = input(f"What would you like? ({choices}): ").lower()
    if coffee_type == "off":
        machine_on = False
    elif coffee_type == "report":
        make_coffee.report()
        money_transfer.report()
    else:
        drink = coffee_menu.find_drink(coffee_type)
        coffee_menu.get_items()
        if make_coffee.is_resource_sufficient(drink):
            if money_transfer.make_payment(drink.cost):
                make_coffee.make_coffee(drink)
