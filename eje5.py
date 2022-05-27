#Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> da un cociente
#<c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario,
#y <c> y <r> son el cociente y el resto de la división entera respectivamente

import re

numero = input("Escribe un numero")
cociente=input("Escirbe ")
if cociente.isdigit() and numero.isdigit():
    print("Cadena válida")
    n=int(numero)
    m=int(cociente)
    divi = n / m
    resto = n % m
    print(n, "entre", m, "da un conciente", divi, "y un resto", resto, "y ", n, m,
          "son los números introducidos por el usuarios,y", divi, "y", resto,
          "son el cociente y el resto de la división entera")
else:
    print("Cadena no válida")