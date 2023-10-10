# A dictionary to store different type of coffee, their ingredients and cost.
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

# A dictionary that has the record of resources available at the starting
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# Calculates the total amount given
def coins():
    print("Please insert coins.")
    quarter = int(input("How many quarters?: "))
    dime = int(input("How many dimes?: "))
    nickel = int(input("How many nickels?: "))
    penny = int(input("How many pennies?: "))
    total = quarter * 0.25 + dime * 0.10 + nickel * 0.05 + penny * 0.01

    # Returns total amount (which will be used to calculate change, if any)
    # Only if it equals to or more than the cost of the coffee
    if total >= MENU[coffee_choice]["cost"]:
        return total
    # Returns 0 if the amount is not sufficient
    else:
        return 0


# Reduces the coffee making resources after a purchase
def reduce_resources():
    resources['water'] -= MENU[coffee_choice]['ingredients']['water']
    resources['coffee'] -= MENU[coffee_choice]['ingredients']['coffee']
    if coffee_choice == 'latte' or coffee_choice == 'cappuccino':
        resources['milk'] -= MENU[coffee_choice]['ingredients']['milk']


# Reports the current available resources in the machine
def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")


# Checks if there's enough resources available for making the requested coffee
def check_resources():
    # Checking if resources available is greater than or equals to the amount required by latte or cappuccino
    # If it is enough, returns 1 else 0
    if coffee_choice != 'espresso':
        if resources["water"] >= MENU[coffee_choice]["ingredients"]["water"] and resources["coffee"] >= MENU[coffee_choice]["ingredients"]["coffee"] and resources["milk"] >= MENU[coffee_choice]["ingredients"]["milk"]:
            return 1
        else:
            return 0
    # Checking the same for espresso
    else:
        if resources["water"] >= MENU[coffee_choice]["ingredients"]["water"] and resources["coffee"] >= MENU[coffee_choice]["ingredients"]["coffee"]:
            return 1
        else:
            return 0


# Loop (machine) will continue to run till machine_off variable becomes true
machine_off = False

while not machine_off:
    coffee_choice = input("What would you like? (espresso/latte/cappuccino): ")
    # Prints out the result from report function
    if coffee_choice == 'report':
        report()
    # Turns off the machine/ ends the loop
    elif coffee_choice == 'off':
        machine_off = True
    else:
        # Checking if the resources are available
        check_value = check_resources()
        if check_value == 0:
            print("Sorry, there's not enough resources.")
        else:
            amount_given = coins()
            # Checking if amount given is sufficient
            if amount_given == 0:
                print("There's not enough money. Money Refunded.")
            else:
                # Calculating the change and rounding off the amount
                cost = MENU[coffee_choice]['cost']
                change = amount_given - cost
                rounded_change = round(change, 2)
                # If exact amount is given, no change will need to be returned
                if change != 0:
                    print(f"Here is ${rounded_change} in change.")

                # Reducing the resources for making the requested coffee
                reduce_resources()
                print(f"Here is your {coffee_choice}. Enjoy!")
