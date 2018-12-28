#!/usr/bin/python3

#First person already registered.
ind1 = 'David'

#Second person already registered.
ind2 = 'Ana'

#Enter the name of the person you are looking for.
ind = input ('Enter name: ')

#Basic info about Carlos.
if (ind == ind1):
    def david ():
        print ('\nFull Name: {fname1}'.format(fname1 = 'David'))
        print ('Last Name: {lnames}'.format(lnames = 'Smith'))
        print ('ID Number: {IDc}'.format(IDc = 4586249 ))
        print ('Passport: {passt}'.format(passt = '15978524'))
        print ('Age: {ag}'.format(ag = 32))
        print ('Profession: {pro}'.format(pro = 'System Administrator'))
        print ('Day of Birth: {DofB}'.format(DofB = '10/12/1985'))
        print ('Nationality: {nation}'.format(nation = 'American\n'))
    david()    

#Basic info about Maria.
elif (ind == ind2):
    def ana ():
        print ('\nFull Name: {fname2}'.format(fname2 = 'Ana'))
        print ('Last Name: {lnames}'.format(lnames = 'Williams'))
        print ('ID Number: {IDm}'.format(IDm = 5697533))
        print ('Passport: {passt2}'.format(passt2 = 'Unknown'))
        print ('Age: {ag2}'.format(ag2 = 30))
        print ('Profession: {pro2}'.format(pro2 = 'Hacker'))
        print ('Day of Birth: {DofB2}'.format(DofB2 = '22/06/1988'))
        print ('Nationality: {nation}'.format(nation = 'British\n'))
    ana()
else:
    print (ind + ' Doesn\'t exist')


#Another feature I want to add to this script is the function that allows
#me to add more persons to the script by using list.
