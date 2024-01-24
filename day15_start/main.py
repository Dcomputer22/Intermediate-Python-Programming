profit = 0
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

def is_resources_sufficient(drink_ordered):
    for item in drink_ordered:
        if drink_ordered[item] >= resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickels = int(input("How many nickels?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    total_amount = round(quarters + dimes + nickels + pennies, 2)
    return total_amount

def transaction_successful(drink_cost, money_inserted):
    global profit
    if money_inserted < drink_cost:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif money_inserted >= drink_cost:
        profit += drink_cost
        change = round(money_inserted - drink_cost, 2)
        print(f"Here's ${change} in change.")
        return True
def make_coffee(drink_ordered, other_resources):
    for item in other_resources:
        if resources[item] >= other_resources[item]:
            resources[item] -= other_resources[item]
    print(f"Here's your {drink_ordered}. Enjoy!")

machine_on = True
while machine_on:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == 'off':
        machine_on = False
    elif coffee_type == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[coffee_type]
        if is_resources_sufficient(drink["ingredients"]):
            payment = process_coins()
            if transaction_successful(drink["cost"], payment):
                make_coffee(coffee_type, drink["ingredients"])