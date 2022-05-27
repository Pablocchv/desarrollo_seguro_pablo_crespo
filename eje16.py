#lista

#De una lista de números, obtener el enésimo mayor número.Tanto el numero enesimo como la lista es introducida por usuario. p.ej. de [1,2,9,8,7,6,5,4] el 4 mayor número es 6.

lista=[]

#while True:
tamlist = input("Escribe el tamaño de la lista ")

if tamlist.isdigit() :
    print("correcto")
    tamlist=int(tamlist)
    if tamlist <9 :
         print("tamaño inferiror al minimo")
    else:
        for i in range(0, tamlist):
            numero = input("Escribe los valores")
            if numero.isdigit():
                print("numero correcto")
            else:
                print("Escribe SOLO NUMEROS")
else:
        print("EScribe un numero")

resultado = sorted(lista)[-9]

print('El enesimo mayor numero de la lista es ' + resultado)

