#!/usr/bin/python3

sandwich_orders = [
        'french dip', 'egg salad',
        'dagwood', 'caprese',
        'clam roll',
        ]
finished_sandwiches = []

while sandwich_orders:
    preparing_sandwich = sandwich_orders.pop()
    print("Preparing " + preparing_sandwich.title() + ' sandwich')
    finished_sandwiches.append(preparing_sandwich)
    print("\nThe following sandwiches are done:")
    for finished_sandwich in finished_sandwiches:
        print(finished_sandwich.title())

print("\n" + finished_sandwich.title())
