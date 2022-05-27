#Escribe uno de los elementos de la lista que previamente creada y que imprima un mensaje cuando se elige un equipo,solo se permiten letras

equipos = ["Barcelona", "Real Madrid", "Manchester United", "Atletico de Madrid","Getafe","Leganes"]

print (equipos[0])
print (equipos[1])
print (equipos[2])
print (equipos[3])
print (equipos[4])
print (equipos[5])

#for i in equipos: #Otra forma de mostrar la lista
 #   print(i,"\n")

while True:
    equipo = input("\n¿Con que equipo te gustaria jugar? Escribelo aqui: ")

    if all(x.isalpha() or x.isspace() for x in equipo): #permitir espacios y solo letras 
        if equipo == "Barcelona":
            print ("Buena eleccion!")
            break
        if equipo == "Real Madrid":
            print (" No es la mejor eleccion!")
            break
        if equipo == "Leganes":
            print("Mejor eleccion imposible!")
            break
        if equipo == "Manchester United":
            print ("Mala eleccion!")
            break
        if equipo == "Ajax":
            print ("Buena eleccion!")
            break
        if equipo == "Getafe":
            print ("Peor eleccion imposible!")
            break
        else:
            print("Elije un equipo de la lista, porfavor.")

    else:
        print ("Por favor, utiliza solo letras.")