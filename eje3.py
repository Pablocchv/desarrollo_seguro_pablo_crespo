
#Escribir un programa que pregunte por consola por los animales de un zoo, separados por asteriscos, y muestre por pantalla cada uno de los animales en una línea distinta.

import re

animal=input("escribes los animales separados por un *")
animales=animal.replace("*", "\n")
patron= "[^(a-zA-Z)(\\s)(\*)]+"
if re.search(patron,animales):
    print("Caracteres invalidos")
else:
    print("Patrón introducido valido")

    #all(i.isalpha() for i in animales)  devuelve verdadero si todos los elementos de un iterable dado son Verdaderos; de lo contrario, devuelve False

    print(animales)