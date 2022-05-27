def validar(dato, tipos):
  for tipo in tipos:
    try:
      return tipo(dato)
    except ValueError:
      pass
  return

while True:
  i= input("Introduzca numero: ")
  x = validar(i, (int, float, complex))
  if x is None:
    print("El dato no es numérico")
  else:
    break
print("Dato introducido correcto:", x)

