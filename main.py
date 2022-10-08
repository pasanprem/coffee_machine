
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

# TODO 1: Create reporting
def print_report():
    print(f"Water : {resources['water']}")
    print(f"Milk : {resources['milk']}")
    print(f"Coffee : {resources['coffee']}")

# TODO 2: Get user request for 1 of 3 types


# TODO 3: See if resources are sufficient
def is_available(a_choice, resource):

    if a_choice == "latte" or a_choice == "cappuccino":
        if (MENU[a_choice]["ingredients"]["water"] > resource["water"]) or \
                (MENU[a_choice]["ingredients"]["milk"] > resource["milk"]) or (
                MENU[a_choice]["ingredients"]["coffee"] > resource["coffee"]):
            return False
        else:
            return True
    else:
        if (MENU[a_choice]["ingredients"]["water"] > resource["water"]) or (
                MENU[a_choice]["ingredients"]["coffee"] > resource["coffee"]):
            return False
        else:
            return True


# TODO 4: Request payment
def get_money(b_choice):
    cost = MENU[b_choice]["cost"] * 100
    print("Please insert coins. ")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    payment = (quarters * 25) + (dimes * 10) + (nickles * 5) + pennies

    if cost <= payment:
        remainder = (payment - cost) / 100
        print(f"Here is your ${remainder} in change. ")
        return True
    else:
        print("Sorry. You do not have enough money")
        return False


# TODO 6: Deduct resources
def deduct_stock(c_choice):
    global resources

    if c_choice == "latte" or c_choice == "cappuccino":
        resources["water"] = resources["water"] - MENU[c_choice]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[c_choice]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[c_choice]["ingredients"]["coffee"]
    else:
        resources["water"] = resources["water"] - MENU[c_choice]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[c_choice]["ingredients"]["coffee"]


# TODO 7: Main function
# Array to make sure the spelling is correct.
all_options = ["espresso", "latte", "cappuccino", "report"]
coffee_options = ["espresso", "latte", "cappuccino"]
choice = input("What would you like? (espresso/latte/cappuccino): ")

if choice in all_options:
    if choice in coffee_options:
        if is_available(choice, resources):
            if get_money(choice):
                print(f"Here is your {choice} ☕️. Enjoy!")
                deduct_stock(choice)
                print("-------------------------------")
                print_report()
        else:
            print(f"Supply not in stock to provide a {choice}")
    else:
        print_report()
else:
    print("Your choice is not valid. ")