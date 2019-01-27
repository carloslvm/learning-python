#!/usr/bin/python3

class Converter():
    def __init__(self, string, integer, lists, dictionary, float_num):
        self.string = string
        self.integer = integer
        self.lists = lists
        self.dictionary = dictionary
        self.float_num = float_num

    def show_integer(self):
        print(str(self.integer))

    def show_list(self):
        print(str(self.lists))

    def show_dictionary(self):
        print(str(self.dictionary))

    def show_float(self):
        print(self.float_num)

    def show_string(self):
        print(self.string)


user_input = Converter("hello",
        45,
        ['solaris', 'ubuntu', 'debian', 'zorin'],
        {'id':1234, 'name':'anna', 'age':25},
        42.345)

user_input.show_integer()
user_input.show_list()
user_input.show_dictionary()
user_input.show_float()
user_input.show_string()
