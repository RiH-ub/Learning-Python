
# 1
def suma(a, b):
    return a + b

resultado = suma(2, 3)
print(resultado) # Salida: 5

# 2
def convertir_mayusculas(cadena):
    return cadena.upper()

texto = "Hola, mundo!"
texto_mayusculas = convertir_mayusculas(texto)
print(texto_mayusculas) # Salida: HOLA, MUNDO!

# 3
def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

resultado1 = es_par(4)
resultado2 = es_par(5)

print(resultado1) # Salida: True
print(resultado2) # Salida: False

# 4
def maximo(lista):
    return max(lista)

numeros = [1, 5, 7, 3, 9]
resultado = maximo(numeros)
print(resultado) # Output: 9


# 5 
def mi_funcion():
    entrada = input("Ingrese un valor: ")
    print("El valor ingresado es:", entrada)

mi_funcion()


# seis
def obtener_nombre():
    nombre = input("Por favor, introduce tu nombre: ")
    return nombre

obtener_nombre()

# 7
def obtener_numero():
    numero_str = input("Introduce un número entero: ")
    numero_int = int(numero_str)
    return numero_int

obtener_numero()
