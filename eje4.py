#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.

num=input("Escribe un numero")
if num.isdigit():
    num=int(num)
    print (num*(num+1)//2)# para evitar que el programa tarde mucho en ejecutar una operacion , expresarlo con notacion cientifica
    print(sum(range(0, num)))
else:
    print("Datos incorrectos")
#Usamos la funcion suma para simplificar el proceso con la funcion isdigit nos aseguramos que siempre se escribe un numero y el primer print garantiza dar un resultado aunque el numero escrito sea muy elevado y la memoria no pueda procesarlo
