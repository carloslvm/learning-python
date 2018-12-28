#!/usr/bin/python3

#Meal list
breakfast = [
            "egg and ham", "sausage and egg",
            "cheese and bacon", "bacon and egg"]

lunch = [
        "sweet potatoe and burrito",
        "broccoli pesto pasta",
        "garlic prawns", "meatball sliders"]

dinner = [
        "angus meatloaf", 
        "roast beef",
        "roast pork loin"]

meals = [breakfast, lunch, dinner]

#Drink list
drinks = ["wine", "fruit juice", "fruit shake"]

#Desserts list
desserts = [
            "s'more ice cream pie",
            "avocado lime cheesecake",
            "cherry pie with almond"]

#General menu list
menus = [meals, drinks, desserts]

#Welcome message
def welcome():
    print ("*" * 60)
    print ("""Welcome. Please select your meal from the menu.
    Press h key to get access to help menu.""")
    print ("*" * 60)

#Help message
def instructions():
    print ("*" * 60)
    print ("""\
    1. Type the name of the element you want to select.
    2. Press "q" key to cancel your selection.
    3. Press "h" key to print this help message.""")
    print ("*" * 60)

def menu():

