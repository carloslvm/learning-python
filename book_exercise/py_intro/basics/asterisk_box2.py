#!/usr/bin/python3

height = int(input('Enter the height of the box: '))
wide = int(input('Enter the width of the box: '))

#a = wide - 2
print('* '*wide)

for box in range(height):
    print('*', ' '*wide, '*')    


print('* '*wide)
        
