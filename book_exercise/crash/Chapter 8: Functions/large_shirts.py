    #!/usr/bin/pyhton3

def first_shirt(message, size='large'):
    print('\nFirst shirt message: ' + message.title())
    print('First shirt size: ' + size.title())

def second_shirt(size, message='i love programming'):
    print("\nSecond shirt message: " + message.title())
    print("Second shirt's size: " + size.upper())

def third_shirt(message, size):
    print("\nThird shirt's message: " + message.title())
    print("Third size's message: " + size.upper())

first_shirt('i love python')
second_shirt(size='xl')
third_shirt('kali linux', 'm')
