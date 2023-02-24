print("Todo sabemos que la formula es la siguiente: # V = (4/3) π r^3 ")

rad = int(input("Dime el radio en cm: "))
vol = (4/3) * 3.1416 * rad**3
resul = format(vol, ".2f")

print("El volumen de la esfera con radio", rad, "cm es de", resul, "cm^3")