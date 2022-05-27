#Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa.
# El programa incorporar funciones crear el fichero con el listín si no existe, para consultar el teléfono de un cliente,
# añadir el teléfono de un nuevo cliente, eliminar el teléfono de un cliente y modificar el nombre o el teléfono de un registro ya creado.
# El listín debe estar guardado en el fichero de texto listin.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.

import os
import re
print("para buscar pulsa la b")
print("si quieres añadir un nuevo registro pulsa la n")
nombre=input("Escribe el nombre de la persona")
patron="[0-9,*,¿?]"
if re.search(patron,nombre):
    print("no se permiten numeros o caracteres especiales")
else:
    print("nombre correcto")

numero=input("Escribe el numero de telefono")

if numero.isdigit() and numero==9:
    print("numero de telefono corrrecto")
else:
     print("numero de telefono o digitos incorrectos")


contac=[nombre,numero] #juntar los apellidos y los nombres y después se separan
contacto= ','.join(contac)
print(contacto)
#archivo= open("/ruta/listin.txt", "w,r,x")#
new=input("pulsa n para añadir un nuevo registro")
buscar=input("buscar un registro")
while  True:
    if new =="n":
        print("se añadira un nuevo registro")

        from pathlib import Path

        fileName = r"listin.txt"
        fileObj = Path(fileName)
        fileObj.is_file()
        resultado = fileObj.is_file()
        resultado = str(resultado)

        if resultado == 'False':
            import os

            archi1 = open("listin.txt", "w")
            print('El archivo no existia,lo acabas de crear')
            archi1.write(contacto)
            archi1.close()
        else:
            import os

            archi1 = open("listin.txt", "a")
            print('se añadira un nuevo registro')
            numero = input('Dime el telefono \n')
            if str(numero.isnumeric()) != 'True':
                print('Solo son validos numeros')
                exit()
            nombre = input('Dime el nombre \n')
            if str(nombre.isalpha()) != 'True':
                print('Solo son validas letras')
                exit()
            numnom = str(numero) + ',' + str(nombre)
            archi1.write(str(numnom) + '\n')
            archi1.close()
    if new  =="s" or buscar =="s":
        break
    else:
        print("caracter invalido")

while True:
    if buscar=="b":
        telabus=input("dime el numero de telefono a buscar")
        if telabus.isdigit():
            print("Bucaresmos el numero de caracter")
            with open("listin.txt","r") as archivo:
                    if telabus in archivo.read():
                        print("Este numero exisite",numero)
                    else:
                        print("este numero no existe")
        else:
            print("el caracter escrito no es un numero o cotiene caracteres que no son numeros")
#file.write("Primera línea" + os.linesep)
#file.write("Segunda línea")
#file.close()

#Volcar los datos en un fichero y que solo pueda escribir las teclas b o s probar eso con un while



