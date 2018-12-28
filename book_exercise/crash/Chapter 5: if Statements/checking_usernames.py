#!/usr/bin/python3

current_users = ['ana', 'andrew', 'shawn', 'david', 'john']
new_users = ['ana', 'steve', 'gabe', 'sarah', 'leo']

for new_user in new_users:
    if new_user not in current_users:
        print (new_user + "-" +"Username available")
    else:
        print (new_user + "-" + "Username is not available, please change it")

