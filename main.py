
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


# TODO 2: Get user request for 1 of 3 types


# TODO 3: See if resources are sufficient
def is_available(a_choice, resource):

    if a_choice == "latte" or a_choice == "cappuccino":
        if (MENU[a_choice]["ingredients"]["water"] > resource["water"]) and \
                (MENU[a_choice]["ingredients"]["milk"] > resource["milk"]) and (
                MENU[a_choice]["ingredients"]["coffee"] > resource["coffee"]):
            return False
        else:
            return True
    else:
        if (MENU[a_choice]["ingredients"]["water"] > resource["water"]) and (
                MENU[a_choice]["ingredients"]["coffee"] > resource["coffee"]):
            return False
        else:
            return True


# TODO 4: Request payment


# TODO 5: Check if payment is sufficient


# TODO 6: Issue return and deduct resources


# TODO 7: Main function
# Array to make sure the spelling is correct.
coffee = ["espresso", "latte", "cappuccino"]
choice = input("What would you like? (espresso/latte/cappuccino): ")

if choice in coffee:
    available = is_available(choice, resources)
    print(available)
