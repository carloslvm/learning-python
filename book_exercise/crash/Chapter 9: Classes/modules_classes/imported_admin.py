#!/usr/bin/python3

from admin2 import Admin

admin = Admin('john', 'doe', 34, 'sysadmin', 
		['can add user', 'can delete user', 'can ban user'])
admin.show_privileges()
