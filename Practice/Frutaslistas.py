"""

def division(a, b):
  try:
    print(a/b)
  except ZeroDivisionError:
    print("No se puede dividir entre cero")
"""
# division

frutas = ["0-Uva", "1-Manzana"]

def elegirFruta(listaFrutas):
  try:
    print(listaFrutas)
    index = int(input("¿Cual es tu fruta favorita?"))
    print(f"Tu fruta favorita es: {listaFrutas[index]}")

  except IndexError:
    print("Esa posicion no existe")
  except ValueError:
    print(f"Tienes que ingresar un numero entre 0 y {len(listaFrutas)-1}")
  finally:
    print("Final msg")


elegirFruta(frutas)