#!/usr/bin/python3

import json

def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username = input("What's your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    username = get_stored_username()
    """Verifying user."""
    login = input('Enter your username: ')
    if login in username:
        greet = "Welcome back, " + username + "!"
        print(greet)
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")

greet_user()
