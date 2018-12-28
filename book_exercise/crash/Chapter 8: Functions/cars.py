#!/usr/bin/python3

def cars(manufacturer, model, **details):
    car_specs = {}
    car_specs['manufacturer'] = manufacturer
    car_specs['model'] = model
    for detail_key, data in details.items():
        car_specs[detail_key] = data
    return car_specs

car = cars('porsche', 'panamera 4S',
        color='black',
        power='440hp',
        length='204.7in',
        height='56.2in',
        price='$115,300.00',)

def show_car():
    for car_detail, car_info in car.items():
        print(car_detail.title() + ' = ' + car_info.title())

show_car()
