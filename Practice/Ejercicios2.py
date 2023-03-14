# Ejercicio 1

valor = float(input("Ingresar el valor: "))
igv = valor * 0.18 + valor

# En caso de tener descuento
if valor > 150000:
  descuento = valor * 0.25 - valor
  print(f"Tienes un descuento de 25% el precio final es de {descuento}")
  
else:
  print(f"El IGV de {valor} es {igv}")
  
# Ejercicio 2

nota1 = int(input("Nota 1: "))
nota2 = int(input("Nota 2: "))
nota3 = int(input("Nota 3: "))
nota4 = int(input("Nota 4: "))

mayor = max(nota1, nota2, nota3, nota4)

print(f"La mayor nota es de {mayor}")

# Ejercicio 3






# Ejercicio 4

llantas = float(inpu("Ingresar el numero de llantas: "))
precio = 800 if llantas < 5 else 700
total = llantas 
