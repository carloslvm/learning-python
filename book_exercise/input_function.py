#!/usr/bin/python3.4

#Mensaje de Bienvenida
print (""" Bienvenido al sistema Python.\n
Antes de continuar, por favor ingrese su nombre y CI\n""")

#Ingreso de datos
name = input ('Ingresar Nombre: ')
CI = input ('Ingresar CI: ')

#Mensaje Final
print ('\nMuchas gracias' +' '+ name +' '+ 'su numero es:' + repr(CI[-2] + CI[-1]))
