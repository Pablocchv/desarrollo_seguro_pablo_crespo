#  Escribir un programa que pregunte el nombre completo del usuario (nombre y apellidos) en la consola
#  y después muestre por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas,
#  otra con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula.
#  El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

nombre=input("Escribe tu nombre")
apellido=input("Escribe tu apellido")
apellidodos=input("Escribe tu segundo apellido")
if nombre.isalpha():
    print(nombre)
else :
    print("Sintaxis incorrecta")
if apellido.isalpha():
    print(apellido)
else :
    print("Sintaxis incorrecta")
if apellidodos.isalpha():
    print(apellidodos)
else:
    print("error")

nombrecompleto=[nombre,apellido,apellidodos]  #juntar los apellidos y los nombres y después se separan
palabra = ' '.join(nombrecompleto)
lista2=[]

print(palabra.lower())
print(palabra.upper())
print(palabra.capitalize())  #Poner tambien los apellidos con las letras en mayusculas
print(palabra.capitalize())

print(nombre.capitalize(),apellido.capitalize(),apellidodos.capitalize())
print(palabra[0].capitalize(),palabra[1].capitalize(),palabra[2].capitalize())


#probar a guardar los elementos en una nueva lista pero con la propiedad capitalazce

#new_string = re.sub('[chars to remove]', '', old_string)

#permitir apellidos internacionales