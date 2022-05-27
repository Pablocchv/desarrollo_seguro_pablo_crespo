#Una farmacia tiene mucho éxito en dos de sus productos: mascarillas y gel hidroalcohólico.
# Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de las mascarillas y geles que saldrán en cada paquete a demanda.
# Cada mascarilla pesa 112 g y cada gel 250 g.
# Escribir un programa que lea el número de mascarillas y geles vendidos en el último pedido y calcule el peso total del paquete que será enviado.

mascarilla=int(112)
gel=int(250)

cantidadm=input("Numero de mascarillas vendidas en el ultimo mes")
cantidadg=input("numero de geles vendidos")
if cantidadm.isdigit():
    print("datos incorrectos")
    if cantidadg.isdigit():
        print("datos correctos")
        print("datos correctos")
        pesotm = mascarilla * cantidadm
        pesotg = gel * cantidadg
        print("el peso de maascarillas sera de", pesotm, "el peso de los geles es de ", pesotg, "y el peso total es de ",
      pesotm + pesotg)
else:
    print("Datos incorrectos")


