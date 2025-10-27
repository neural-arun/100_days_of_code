"""chai_wala.py."""

MENU = {
    "masala": {
        "ingredients": {
            "water": 50,
            "milk": 100,
            "tea_leaves": 18,
            "sugar": 10,
            "masala": 5,
        },
        "cost": 15,
    },
    "ginger": {
        "ingredients": {
            "water": 60,
            "milk": 90,
            "tea_leaves": 20,
            "sugar": 10,
            "ginger": 7,
        },
        "cost": 12,
    },
    "elaichi": {
        "ingredients": {
            "water": 60,
            "milk": 90,
            "tea_leaves": 20,
            "sugar": 10,
            "cardamom": 4,
        },
        "cost": 10,
    },
}

profit = 0
resources = {
    "water": 500,  # ml
    "milk": 300,  # ml
    "tea_leaves": 100,  # g
    "sugar": 80,  # g
    "ginger": 30,  # g
    "masala": 20,  # g
    "cardamom": 20,  # g
}

# TODO (arun yadav): Start your code here!


print("We have: \n Elaichi - 10 rupees\n Masala - 15 rupees\n Ginger - 12 rupees")
user_input = input("What would you like? (masala/ginger/elaichi): ")
