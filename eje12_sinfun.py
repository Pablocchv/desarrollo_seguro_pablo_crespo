import re

patron= "[0-9]"
cadena=input("Escribe una palabra o frase")
if re.search(patron,cadena):
    print("no se permiten numeros")
else:
    print("correcto")
    cadena = cadena.split()
    palabra = {}  # diccionario vacio
    if all(x.isalpha() or x.isspace() for x in cadena):
            for i in cadena:  # recoremos la cadena
                if i in palabra:  # añadimos las palabras al diccionario
                     palabra[i] += 1
                else:
                    palabra[i] = 1
    print(palabra)

    max_palabra = ''
    max_freq = 0  # indicamos que la mayor frecuencia es 0 y después igualamos la variable
    for palabra, fre in palabra.items():  # Devuelve una lista de tuplas claves:valor
        if fre > max_freq:
            max_palabra = palabra
            max_freq = fre
    print("el maximo de palabras es",max_palabra, "y se repite", max_freq)
