print("Bienvenidos a peleas de Gatos")
print("-----------------------------")

name = input("Introduce tu nombre: ")
print("-----------------------------")
print(f"¡Bienvenido al juego, {name}!")
print("ᕙ⁠(⁠⇀⁠‸⁠↼⁠‶⁠)⁠ᕗ")
print("-----------------------------")

print("¡Escoge tu gato!")
cat = input("Polar o Titi: ")
print("××××××××××××××××××")

if cat == "polar" or cat == "Polar":
  print("¡Escogiste a Polar!")
  print("Vida: 70")
  print("Daño: 300")
  print("Movilidad: 200")
  op = input("polar inicia: ")

elif cat == "titi" or cat == "Titi":
  print("¡Escogiste a Titi!")
  print("Vida: 100+")
  print("Daño: 210+")
  print("Movilidad: 70")

print("-----------------------------")
print("")