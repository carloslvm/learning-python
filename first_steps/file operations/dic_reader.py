#!/usr/bin/python3

import json

filename = 'user_info.json'
try:
	with open(filename) as data:
		content = json.load(data)
		for k, v in content.items():
			print(k, ":", v)
except FileNotFoundError:
	print('File does not exist.')
