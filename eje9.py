#Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “BASTA!” que terminará
import re
palabra=input("Escribe una palabra")
patron='[a-z,A-Z,!]'
while palabra!="BASTA!":
    if re.search(patron,palabra):
        print(palabra)
        palabra=str(input("Escribe una palabra"))
    else:
        print("Cadena incorrecta escribe un valor valido")
        palabra = str(input("Escribe una palabra"))