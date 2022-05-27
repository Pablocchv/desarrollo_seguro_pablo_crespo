#Escribir una función que reciba una muestra de números y devuelva los valores atípicos,
# es decir, los valores cuya puntuación típica sea mayor que 3 o menor que -3.
# Nota: La puntuación típica de un valor se obtiene restando la media y dividiendo por la desviación típica de la muestra.

import re
import random
import statistics

lista=[]

for i in range (12):
    lista.append(random.randint(-3,10)) #la lista se rellena de valores aleatorios entre 0 y 30 con un maximo de 12 numeros
print("los valores de la lista son ",lista)
#usamos la funcion media para que cualcula la media de los valores de la lista
med=statistics.mean(lista)
print("La media es ",med)

##Calcular la desviación tipica con la función statitcs.pstdev
desviacion=statistics.pstdev(lista)
print("La desviación tipica  es",desviacion)
contador=0
#recorremos la lista y calculamos la putuación tipica
while contador< len(lista):
    resta=lista[contador]-med
    tipico=resta/desviacion
    if tipico <=-3 or tipico>=3:
        print("Los numeros con una puntuación tipica mayor que 3 o menor -3 son",lista[contador])
    elif tipico >= -3 and tipico <= 3:
        print('No hay numeros con una gran puntuacion tipica')
    else:
        print("no hay numeros con una puntuación tipica")
    contador=contador+1
    print(tipico)