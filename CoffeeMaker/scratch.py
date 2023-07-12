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

#TODO: 1. Create loop to ask for input and turn off machine

coffee = input("What would you like? (espresso/latte/cappuccino): ")


def checkCoffee(Menu,coffee):                            #key calls for 2nd argument, def is used for arguments, check if its in dictionary
    if coffee in MENU.keys():                            #if coffee is in M.keys, print yes or no
        return coffee                                    #return: saves the value
    elif coffee == "report":
        print(str(resources))
        return
    else:
        print("not in menu")
        return

def checkResources(bev):
    if(bev == "espresso"):
        resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
        resources["milk"] = resources["milk"] - MENU["espresso"]["ingredients"]["milk"]
        return resources["water"]

        return resources["coffee"]

        return resources["milk"]


while coffee!= "off":
    choice = checkCoffee(MENU,coffee)
    print(checkResources(choice))
    coffee = input("What would you like? (espresso/latte/cappuccino): ")



