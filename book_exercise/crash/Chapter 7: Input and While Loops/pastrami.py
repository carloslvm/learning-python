#!/usr/bin/python3

sandwich_orders = [
        'pastrami', 'pastrami',
        'pastrami', 'french dip',
        'dagwood', 'caprese',
        'clam roll'
        ]
finished_sandwiches = []

print("The deli has run out of pastrani")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    preparing_sandwich = sandwich_orders.pop()
    print('Preparing ' + preparing_sandwich + ' sandwich')
    finished_sandwiches.append(preparing_sandwich)
    print("\nThe following sandwiches are done:")
    for finished_sandwich in finished_sandwiches:
        print(finished_sandwich.title())
print('\n', finished_sandwiches)
