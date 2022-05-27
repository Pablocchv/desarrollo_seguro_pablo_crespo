#Escribir una función que calcule el total de una factura tras aplicarle el IVA.
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total de la factura.
# Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%
import re
preciofin=int(0)
patron="[0-9]"
importsiniva=input("Escribe el importe de la factura sin iva")

if re.search(patron,importsiniva):
    print("Correcto")
    importsi = int(importsiniva)
    ivainp = input("Escribe el porcentaje de IVA para aplicar")
    if ivainp == "":
        ivainp = int(21)
        ivainp = int(ivainp)
        preciofin = importsi + importsi * ivainp / 100
        print("El precio final es de", preciofin)
    elif re.search(ivainp,patron):
        print("correcto")
        ivainp = int(ivainp)
        preciofin = importsi + importsi * ivainp / 100
        print("El precio final es de", preciofin)

    else:
        print("incorrecto")



else:
    print("no")




#poner restricciones al iva y al importe y que después se aplique , poner por defecto un 21