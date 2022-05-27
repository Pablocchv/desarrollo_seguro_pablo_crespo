#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34,
#y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa que pregunte por un número de teléfono con este formato
#y muestre por pantalla el número de teléfono sin el prefijo y la extensión.
#Además, debe reconocer el prefijo la comunidad autónoma.
import re
patron="[^(*)(0-9)(-)]+"
patron2="[^(a-zA-Z)(¿?)]"
patron3="^[+]{0,1}[0-9]{2}-[0-9]{9}-[0-9]{2}$"
#impedir que se escriba letras
tel=input("Escribe el numero en siguiente formato  +xx-xxxxxxxxx-xx:")
if re.search(patron3,tel):
    print("Correcto")
    print("El numero de telefono es", tel[4:-3])
    telefono = tel[4:13]

    pre = tel[4:7]
    prefijo2 = tel[4:6]
    prefijo = int(pre)
    prefijo2 = int(prefijo2)
    if telefono.isdigit():

        if len(telefono) > 9 or len(telefono) < 9:
            print("Has introducido más de nueve caracteres en el telefono")
        else:
            if prefijo in (980, 981, 982, 986):
                print("Galicia")
            elif prefijo in (942):
                print("Cantabria")
            elif prefijo in (945, 943, 944):
                print("Pais Vasco")
            elif prefijo in (948):
                print("Comunidad Foral de Navarra")
            elif prefijo in (941):
                print("La rioja")
            elif prefijo in (920, 947, 987, 979, 923, 921, 975, 983, 980):
                print("Castilla y león")
            elif prefijo in (974, 978, 976):
                print("Aragón")
            elif prefijo in (965, 966, 964, 960, 961, 962, 963):
                print("Comunidad Valenciana")
            elif prefijo in (972, 973, 977, 93):
                print("Catalunya")
            elif prefijo in 968:
                print("Región de Murcia")
            elif prefijo2 == 91:
                print("Comunidad de Madrid")
            elif prefijo in (950, 956, 957, 958, 959, 953, 951, 954):
                print("Andalucia")
            elif prefijo in (924, 927):
                print("Extremadura")
            elif prefijo in (926, 969, 949, 925):
                print("Castilla la Mancha")

else:
    print("patron incorrecto")





#probar en el patron distintos caracteres para ver coomo funciona

