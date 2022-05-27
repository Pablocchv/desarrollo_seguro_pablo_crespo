#Escribir un programa en el que se pregunte al usuario por una frase y una letra,
#y muestre por pantalla el número de veces que aparece la letra en la frase y el número total de caracteres de la frase sin espacios en blanco.
import re

frase=str(input("Escribe una frase"))
caracter=str(input("Escribe el caracter a buscar"))
patron= "[0-9]"
if re.search(patron,frase):
        print("no se permiten numeros")
elif re.search(patron,caracter):
        print("no se permiten buscar numeros")
else:
    if all(x.isalpha() or x.isspace() for x in frase):  # permitir espacios y solo letras
                numc = frase.count(caracter)
                sine = frase.replace(' ', '')
                if sine.isalpha():
                        tam = len(sine)
                        print(" el caracter ",caracter , "aparece un total de",numc,"el tamaño de la cadena es de ",tam)

#Probar con re. search si encuentra un caracter del patron en el nombre o el caracteres devolver un error
