#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia.
#Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

def contar_palabras(cadena):
    cadena=cadena.split()
    palabra = {} # diccionario vacio
    for i in cadena: #recoremos la cadena
        if i in palabra:  #añadimos las palabras al diccionario 
            palabra[i] +=1
        else:
            palabra[i] =1
    return palabra

def mas_comun (palabra):
    max_palabra = ''
    max_freq=0 #indicamos que la mayor frecuencia es 0 y después igualamos la variable
    for palabra,fre in palabra.items(): #Devuelve una lista de tuplas claves:valor
        if fre > max_freq:
            max_palabra=palabra
            max_freq=fre
    return max_palabra,max_freq
cadena=input("Escribe")
print(contar_palabras(cadena))
print(mas_comun(contar_palabras(cadena)))