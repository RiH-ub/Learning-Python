def saludo(nom):
  print("Hola "+ nom + " buenas ")

saludo("Renzo")
saludo("Ceci")

def sumar(a, b):
  print(a + b)

sumar(22, 8)
sumar(2, 2)


def multiplicar(a, b):
  result = a * b
  return result

result = multiplicar(3, 3)
print(result)



def validarIngreso():
  edad = int(input("Ingrese edad: "))

  if edad >= 18: 
    mensaje = "Eres mayor de edad, puedes acceder"
    
  elif edad >= 14:
    mensaje = "Eres menor de edad, debes tener autorizacion"
    
  elif edad > 6: 
    mensaje = "Eres muy pequeño"
    
  else:
    mensaje = "Definitivamente, no puedes ingresar"

  return mensaje

print(validarIngreso())


def validarIngreso(edad):
  if edad >= 18:
    return "Eres mayor de edad, puedes acceder" 
  elif edad >= 14:
    return "Eres menor de edad, debes tener autorizacion" 
  elif edad > 6:
    return "Eres muy pequeño" 
  else:
    return "Definitivamente, no puedes ingresar"


verficarIngreso() # Sin_ retorno

ingreso = validarIngreso(21) # Con retorno

print(ingreso)