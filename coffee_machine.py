# TODO 1: Dictionaries containing all the needed data for the coffee
MENU = {
    "espresso": {
        "ingredients": {
           "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0


def is_resources_sufficient(drink_ordered):
    for item in drink_ordered:
        if drink_ordered[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def transaction_successful(drink_cost, money_inserted):
    if money_inserted >= drink_cost:
        change = round(money_inserted - drink_cost, 2)
        print(f"Here is your {change} change")
        global profit
        profit += drink_cost
        return True

    elif money_inserted <= drink_cost:
        print("Sorry that's not enough money. Money refunded")
        return False


def make_coffe(drink_name, other_resources):
    for item in other_resources:
        if resources[item] >= other_resources[item]:
            resources[item] -= other_resources[item]
    print(f"Here is your ☕ {drink_name}. Enjoy!")

is_on = True
while is_on:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")
    if coffee_type == "off":
        is_on = False
    elif coffee_type == "report":
        print(f"Water: {resources['water']}")
        print(f"Water: {resources['milk']}")
        print(f"Water: {resources['coffee']}")
        print(f"Money: {profit}")
    else:
        drink = MENU[coffee_type]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(drink["cost"], payment):
                make_coffe(coffee_type, drink["ingredients"])

