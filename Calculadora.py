def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

while True:
  
  print()
  print()
  print("1)      Suma         |")
  print("2)      Resta        |")
  print("3)  Multiplicación   |")
  print("4)     División      |")
  
  op = input("Selecciona el tipo de operación a realizar: ")
  
  print()
  num1 = int(input("Primer número: "))
  num2 = int(input("Segundo número: "))

  if op == "1":
    print(num1, "+", num2, "=", sumar(num1, num2))

  elif op == "2":
    print(num1, "-", num2, "=", restar(num1, num2))

  elif op == "3":
    print(num1, "x", num2, "=", multiplicar(num1, num2))

  elif op == "4":
    print(num1, "÷", num2, "=", dividir(num1, num2))

  else:
    print("Entrada no válida")

}