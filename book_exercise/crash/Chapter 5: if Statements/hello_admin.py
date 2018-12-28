#!/usr/bin/env python3

usernames = ["jsmith", "dscot", "awilliams", "fshawn", "admin"]

for username in usernames:
    if username == "admin":
        print ("Hello " + usernames[-1] + 
                " Do you want to see the status report?")
    else:
        print ("Hello " + username + 
                " Thank you for login again ")

