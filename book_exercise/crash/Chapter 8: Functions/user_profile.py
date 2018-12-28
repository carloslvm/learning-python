#!/usr/bin/python3

def create_profile(first, last, **extra_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in extra_info.items():
        profile[key] = value
    return profile

user_profile = create_profile('anna', 'williams',
                            country='england',
                            language='english',
                            age = 30,
                            profession='system administrator')

def show_profile():
    for key, value in user_profile.items():
        print(key.title() + ' = ' + str(value).title())

show_profile()
