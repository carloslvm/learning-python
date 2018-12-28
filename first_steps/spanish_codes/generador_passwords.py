#!/usr/bin/python3.4

#This is the first message to show to the user.
Message1 = """Bienvenido a PYSystem Corporation. \n
Antes de proceder, llene el siguiente formulario por favor."""

#This is the second message after filling out the form.
Message2 = '''Muchas gracias por tomarse el tiempo de llenar el formulario. 
De acuerdo a la informacion que nos acaba de proveer, procedemos a 
mostrarle su password para sus futuras operaciones.'''

#Third and final Message called TROLL.
Message3 = "Su password ha sido enviado a su escritorio en un documento de texto."

#Here prints the first message.
print (Message1)

#These are the questions that must be answered by the user.
#The answers of these questions are required to generate the password.
name = input("Por favor introduzca su nombre: ")
ID = input ("Por favor introduzca su numero de identificacion: ")
profession = input ("Por favor introduzca su profesion: ")
country = input ('Por favor introduzca su pais de procedencia: ')
birthday = input ('Por favor introduzca su fecha de nacimiento: ')
city = input ('Por favor introduzca el estado donde vive: ')
phone = input ("Por favor introduzca su numero de telefono: ")
pwork = input ('Tiene experiencia en el campo de la tecnologia e informacion?: ')
special = input('Por favor introduzca al menos tres caracteres especiales: ')

#Password to create. Here is where the password is generated.
password = name[2]+ID[5]+profession[3]+country[4]+birthday[7]+city[2]+phone[5]+pwork[1]+special[1]

#Showing second message and password.
print ('\n' + Message2 +" "+ password +'\n')

#Showing third message.
print (Message3 + '\n')

#Here I send the password to Desktop as a text file.
file = open ("/home/user/Desktop/password.txt","w" )
file.write (password)
file.close()
