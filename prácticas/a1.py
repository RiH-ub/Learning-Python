# Calcular el valor de una esfera = 4/3) π r^3
print("Todo sabemos que la formula es la siguiente: # V = (4/3) π r^3 ")

rad = int(input("Dime el radio en cm: "))
vol = (4/3) * 3.1416 * rad**3
resul = format(vol, ".2f")

print("El volumen de la esfera con radio", rad, "cm es de", resul, "cm^3")



# Calcular el volumen de un cono = 1/3πr^2 altura
radio = int(input("Dime el radio en cm: ")) 
altura = int(input("Dime la altura en cm: "))

volumen = (1/3) * 3.14159 * radio**2 * altura
print("El volumen de un cono con radio", radio, "cm y altura", altura, "cm es de", volumen, "cm^3")



# Calcular el valor de un cubo = C^3
lado = int(input("Longitud de lado: "))
volumen_cubo = lado ** 3

print("El volumen del cubo es:", volumen_cubo)




# Convertir minutos a segundos
min = int(input("Minutos: "))
seg = min * 60

print(min, "minutos son", seg, "segundos.")



# Escribe pseudocódigo que calcule el perímetro de un círculo
rad = int(input("Radio: "))

PI = 3.14159

per = 2 * PI * rad

print("El perímetro del círculo es:", per)

