# Nuevo
pol = str()
tit = str()


while True:
  print("A Polar")
  print("B Titi")
  cat = input()
  print("××××××××××××××××××")

  if cat == "a":
    print("¡Escogiste a Polar!")
    print("Vida: 70")
    print("Daño: 300")
    print("Movilidad: 200")
    print("¿Que haras?: \n A. Mordida \n B. Arañazo")

    while True:
      pol = input()
      
      if not (pol == "a" or pol == "b"):
        print("Entrada no valida")
      if (pol == "a" or pol == "B"): break

    if pol == "a":
      print("Polar uso mordida")

    elif pol == "b":
      print("Polar uso arañazo")
    
  elif cat == "b":
    print("¡Escogiste a Titi!")
    print("Vida: 100")
    print("Daño: 210")
    print("Movilidad: 70")
    print("¿Que haras?: \n A. Llorar \n B. Escapar")

    while True:
      tit = input()
     
      if not (tit == "a" or tit == "B"):
        print("Entrada no valida")
      if (tit == "a" or tit == "B"): break

    if tit == "a":
      print("Titi se pone a llorar")

    elif tit == "b":
      print("Titi escapa muy lejos")

