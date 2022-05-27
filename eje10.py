#Escribir un programa que almacene los números de 0 a 35 en una lista, elimine de la lista los números que ocupen posiciones múltiplos de 3,
# y muestre por pantalla la lista resultante.

lista=[]

for i in range (1,35):
    lista.append(i)

# EL -1 lo que hace es recorrer la lista hasta el final  y con el if indicamos si es modulo de 3 para
tam=len(lista)
for i in  range (len(lista),0,-1):
    if i %3 ==0 :
            lista.pop(i-1)  #.pop elimina de la lista
print (lista)


#Buscar que la lista solo tiene numeros