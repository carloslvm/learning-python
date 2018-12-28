#!/usr/bin/python3

ana_id = 4589
mike_id = 5637

while True:
    code_number = int(input("Enter person's ID number please: "))
    if code_number == 753:
        break

    if code_number == ana_id:
       print ('{ana}'.format(ana = {'Name' : 'Ana Williams', 'Country' : 'England', 'Age' : 37}))
    elif code_number == mike_id:
       print ('{mike}'.format(mike = {'Name' : 'Mike Smith', 'Country' : 'USA', 'Age' : 35}))
    else:
        print (repr(code_number) + ' ' + 'Does not exist')

print ('The loop is over.')
