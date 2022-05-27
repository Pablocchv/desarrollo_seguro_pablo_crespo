suma=0
num=int(input("Escribe el numero hasta que quieres sumar"))
for i in range (1,num):
    print(i)
    suma=i+suma

print("La suma hasta el",num,"es de ",suma ,end= "")
print()
suma2=0
num2=int(input("Escribe otro numero que suma"))
contador=0
while contador!=num2:
    suma2=suma2+num2
    contador=contador+1
print(suma2)