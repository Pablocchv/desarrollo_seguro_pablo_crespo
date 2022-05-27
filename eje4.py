#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.

suma=0
lista=[]
num=input("Escribe un numero")
if num.isdigit():
    num=int(num)
    for i in range(0,num):
        lista.append(i)
        sumaf=sum(lista)

    print(sumaf)
else :
    print("Datos incorrectos")
#función sum en pyhton

   #for i in range (1,num+1):
     #   print(i)
        #suma=suma+i
