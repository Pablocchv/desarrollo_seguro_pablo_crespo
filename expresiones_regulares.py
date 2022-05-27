import re

cadena="Vamos a aprender expresiones regulares en Python. Python es una lenguaje de sintaxis sencillas"

print(re.search("aprender",cadena)) # llama a la función serach de re para buscar en la variable cadena, primero se indica donde bucar y luego donde tiene que buscar

textoabuscar="aprender"

if re.search(textoabuscar,cadena) is not None: #Si encuentra el texto
    print("he encontrado el texto")
else:
    print("no he encotnrado el texto")


textoencontrado=re.search(textoabuscar,cadena)

print(textoencontrado.start()) #star: numero de caracter donde empieza el texto
print(textoencontrado.end()) #end: numero de caracter donde acaba el texto
print(textoencontrado.span()) #star: numero de caracter donde empieza el texto y donde acaba pero en una tupla
print(re.findall(textoabuscar,cadena)) #re.findall busca todos los parametros que indicamos en donde y el que nos muestra las palabras
print(len(re.findall(textoabuscar,cadena))) #longitud de la lista buscando los elementos

lista_nombres=['Ana Gomez', 'María Martín','Sandra López','Santiago Martín','Sandra Perez']

for element in lista_nombres:
    if re.findall ('^Sandra',element):  # el ^ busca los elementos que empiezan por Sandra y que recorra el elemento
        print(element)

for elemento2 in lista_nombres:
    if re.findall("Martín$",elemento2): #eL $ no busca las concidencias de texto que terminan por Martín
        print(elemento2)

lista_tarjetas = ["RTX 3090","GTX 1050","GTX 1650 Ti","RTX 2070","GT 1030","P 100"]



for elemento in lista_tarjetas:
    if re.findall('[P]',elemento):
            print("tarjetas con la palabra P",elemento)
for elemento in lista_tarjetas :

    if re.findall('[P]TX', elemento):  # Con los elementos dentro del corchete los que indicamos es que es nos busca siguiendo un patron

        print(elemento)
coches=["turismo","todoterreno","moto","camion","camión"]

for elemento in coches: #Busca dentro de la lista elementos con el patron que empiecen por cami y contengan
    if re.findall('cami[oó]n',elemento):
        print(coches)

nombres=["Ana","Celia","Maria","Pedro","Sandra","Rosa"]

for i in nombres:
    if re.findall('[o-t]',i):  #Busca dentro de un rango de letras de la o a la t, Distingue entre mayus y minus
        print(i)
for i in nombres:
    if re.findall('^[o-t]',i):  #Busca dentro de un rango de letras de la o a la t en este caso que empicen por la letra T
        print(i)

ciudad=["Ma1","Ma2","Ba1","Se1","Bi1","Va1","Ma4","Ma5","MaC","MaA","MaB"]

for i in ciudad:
    if re.findall('Ma[0-3]',i): #Buscar con un rango de numeros y un patron
        print(i)

for i in ciudad:
    if re.findall('Ma[^0-3]',i): #Buscar los elementos en la negación de ese rango
        print(i)

for i in ciudad:
    if re.findall('Ma[0-5A-D]',i):
        print(i)
ciudad2=["Ma.1","Ma2","Ba1","Se1","Bi1","Va1","Ma:4","Ma5","Ma.C","MaA","MaB"]
for i in ciudad2:
    if re.findall('Ma[.:]]',i):
        print(i)
#Funciones searh y match
nombre1="Sandra Lopez"
nombre2="Antonio Gómez"
nombre3="María López"
nombre4="Lara tenor"
nombre5="Jara Garcia"
cadena12="Antonio Gómez"
cadena22="4564588581"
cadena13="a4564588581"
if re.match("Sandra",nombre1,re.IGNORECASE): #Distingue entre mayusclas y minusculas el ignonere case ignora las mayusculas

    print("Encontrado")
else:
     print("no encontrado")

if re.match(".ara",nombre4,re.IGNORECASE):  #El punto lo que hace es ignorar el resto de parametros

    print("Encontrado")

if re.match("\d",cadena22):   #La expresion regular \d  con la funcion si la cadena empieza por un numero o no
    print("hemos encontrado el numero")
else :
        print("no hemos encontrado el numero")

#Función search Busca en toda la cadena de texto

if re.search("Lopez",nombre1,): #parametro a buscar,variable donde va a buscar, y flag
    print("Nombre Encontrado")
else:
    print("no hemos encontraod el ")

cod1="fwougegjepgjegpejgpejgepgpggpgegegijegjegjegpjgpjgpwjpjfpodfpjpedf"
cod2="qwertyghujikopiuyftgvbhnjuikosdfghjklswdfghjkl71asdfghjkl"
cod3="wertyuiopsdfghjklñxcvbnmwsedrftghyuji"
if re.search("71",cod2):
    print("Codigo encontrado")
else :
    print("codigo NO encontrado")