# Bucles
# Variables de inicialización (estado) 
# while condición:
  # codigo a repetir
  # Variable de control 

# 
# Tablas de operaciones

print("Tabla de operaciones")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

op = input("Escoger una opcion: ")
num = int(input("Ingresa el valor: "))

def suma(num):
  for i in range(1, 13):
    print(f"{i} + {num} = {i+num}")

def resta(num):
  for i in range(num, 13+num):
    print(f"{i} - {num} = {i-num}")

def multiplicar(num):
  for i in range(1, 13):
    print(f"{i} x {num} = {i*num}")

def dividir(num):
  for i in range(num, 13 * num, num):
    print(f"{i} / {num} = {int(i/num)}")

if op == "1":
  print("Tabla de sumar")
  suma(num)

elif op == "2":
  print("Tabla de restar")
  resta(num)
  
elif op == "3":
  print("Tabla de multiplicar")
  multiplicar(num)

elif op == "4":
  print("Tabla de dividir")
  dividir(num)
  
else:
  print("Entrada invalida")
              


