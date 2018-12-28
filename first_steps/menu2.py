#!/usr/bin/python3

#Meal and price
breakfast = {
        "egg and ham":10,
        "sausage and egg":15,
        "cheese and bacon":20,
        "bacon and egg":25,
        }

lunch = {
        "sweet potato and burrito":40,
        "broccoli pesto pasta":45,
        "garlic prawns":50,
        "meatball sliders":55,
        }

dinner = {
        "angus meatloaf":30,
        "roast beef":35,
        "roast pork loin":40,
        }

#Drinks and prices
drinks = {
        "wine":65,
        "fruit juice":15,
        "fruit shake":25,
        }

#Desserts
desserts = {
        "s'more ice cream pie":38,
        "avocado lime cheesecake":24,
        "cherry pie with almond":33,
        }

#Welcome message
def welcome():
    print("*" * 60)
    print("""\
            Welcome. Please make your order from the menu:
            1.Breakfast.
            2.Lunch.
            3.Dinner.
            4.Drinks.
            5.Desserts.
            Press the "h" key to open the help manual.
            
            WARNING: This program is case sensitive.
                     Please use lowercase letters."""
            )
    print("*" * 60)

#Breakfast menu
def menu_breakfast():
    for food_b, price_b in sorted(breakfast.items()):
        print("\nFood: " + food_b.title())
        print("Price: " + "$" + repr(price_b))
    select_breakfast = input("Please select your food: ")
    if select_breakfast not in breakfast:
        print("Sorry that option is not available.")
    else:
        print("Thank you for your choice.")
        print("You have selected: " + select_breakfast)
        
    if select_breakfast == 'c':
        print("Operation cancelled")

#Lunch menu
def menu_lunch():
    for food_l, price_l in sorted(lunch.items()):
        print("\nFood: " + food_l.title())
        print("Price: " + "$" + repr(price_l))
    select_lunch = input("Please select your food: ")
    if select_lunch not in lunch:
        print("Sorry that option is not available.")
    else:
        print("Thank you for your choice.")
        print("You have selected: " + select_lunch)
        
    if select_lunch == 'c':
        print("Operation cancelled.")

#Dinner menu
def menu_dinner():
    for food_d, price_d in sorted(dinner.items()):
        print("\nFood: " + food_d.title())
        print("Price: " + "$" + repr(price_d))
    select_dinner = input("Please select your food: ")
    if select_dinner not in dinner:
        print("Sorry that option is not available.")
    else:
        print("Thank for your choice.")
        print("You have selected: " + select_dinner)
        
    if select_dinner == 'c':
        print("Operation cancelled.")

#Drinks menu
def menu_drinks():
    for drink, price_dr in sorted(drinks.items()):
        print("\nDrink: " + drink.title())
        print("Price: " + "$" + repr(price_dr))
    select_drink = input("Please select your drink: ")
    if select_drink not in drinks:
        print("Sorry that option is not available.")
    else:
        print("Thank you for your choice: ")
        print("You have selected: " + select_drink)
        
    if select_drink == 'c':
        print("Operation cacelled.")

#Desserts menu
def menu_desserts():
    for dessert, price_dr in sorted(desserts.items()):
        print("\nDessert: " + dessert.title())
        print("Price: " + "$" + repr(price_dr))
    select_dessert = input("Please select your dessert: ")
    if select_dessert not in desserts:
        print("Sorry that option is not available.")
    else:
        print("Thank you for your choice.")
        print("You have selected: " + select_dessert)
                
    if select_dessert == 'c':
        print("Operation cancelled")

#Manual
def manual():
    print("*" * 60)
    print("""\
            1.To select; type the name of the item you
            want to select.
            2.Press the "q" key to quit.
            3.Press the "c" key to cancel.
            4.Press the "h" key to print this help info.
            5.Press the "m" key to print the initial menu.
            """)
    print("*" * 60)

#Main program
welcome()
while True:
    command = input('What would you like to order: ')
    if command == 'breakfast':
        menu_breakfast()
    elif command == 'lunch':
        menu_lunch()
    elif command == 'dinner':
        menu_dinner()
    elif command == 'drinks':
        menu_drinks()
    elif command == 'desserts':
        menu_desserts()
    elif command == 'h':
        manual()
    elif command == 'm':
        welcome()
    elif command == 'q':
        print("""\
                Thank you for coming.
                Feel free to come back anytime.""")
        break
    else:
        print("Unknown command.")

