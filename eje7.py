#En una determinada empresa, sus productos son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando,
# traduciéndose en mejores opiniones.
# Los puntos que pueden conseguir los productos pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
# A continuación, se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de reputación conseguida en cada nivel es de 1.5 puntos multiplicada por la puntuación del nivel.
#Mal producto: 0.0
#Aceptable: 0.4
#Reseñable: 0.6 o más
#Escribir un programa que lea la puntuación del producto e indique su nivel de evaluación, así como la reputación del producto.

malp=float(0.0)
acept=float(0.4)
rese=float(0.6)
val=float(1.5)
def validar(dato, tipos):
  for tipo in tipos:
    try:
      return tipo(dato)
    except ValueError:
      pass
  return None

while True:
  pun= input("Introduzca numero: ")
  x = validar(pun, (int, float, complex))
  if x is None:
    print("El dato no es numérico")
  else:
    break
print("Dato introducido:", x)

if x == 0.4 :
  print("la puntuación del producto es",x*val)
elif x==0.6:
  print("la puntuación del producto es", x * val)
elif x==0.0:
  print("la puntuacion es de",x*val)



