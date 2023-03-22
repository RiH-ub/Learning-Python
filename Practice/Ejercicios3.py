# Realiza un algoritmo que calcule el factorial de un número entero positivo utilizando un bucle while en Python. El algoritmo debe pedir al usuario que introduzca el número para el cual desea calcular el factorial y mostrar el resultado por pantalla.

numero = int(input("Introduce un número entero positivo: "))
num = numero

# Formula del factorial
factorial = 1
while num > 1:
    factorial *= num
    num -= 1

print(f"El factorial de {numero} es: {factorial}")




# Implementa un algoritmo que ordene una lista de números enteros utilizando el algoritmo de ordenamiento por selección en Python. El algoritmo debe pedir al usuario que introduzca los números de la lista y mostrar la lista ordenada por pantalla.

# Pedir al usuario que introduzca los números de la lista
orden = []
while True:
    numero = input("Introduce un número entero ('Fin' para terminar): ")
    if (numero == "Fin" or numero == "fin"):
        break
    orden.append(int(numero)) # El método "append()" en Python es utilizado para agregar un elemento al final de una lista.

# Algoritmo de ordenamiento
for i in range(len(orden)):
    minimo = i
    for j in range(i+1, len(orden)):
        if orden[j] < orden[minimo]:
            minimo = j
    orden[i], orden[minimo] = orden[minimo], orden[i]

# Mostrar la lista ordenada
print(f"La lista ordenada es: {orden}")




# Implementa un algoritmo que busque el número más grande y el número más pequeño en una lista de números enteros utilizando un bucle for en Python. El algoritmo debe pedir al usuario que introduzca los números de la lista y mostrar los resultados por pantalla.

numeros = []
elementos = int(input("Introduce el tamaño de tu lista: "))

for i in range(elementos):
    num = int(input("Introduce un número: "))
    numeros.append(num) #El método append() en Python es utilizado para agregar un elemento al final de una lista.

print(f"El número más grande es: {max(numeros)}")
print(f"El número más pequeño es: {min(numeros)}")




# Realizar un algoritmo que determine si un número entero positivo es primo o no en Python. El algoritmo debe pedir al usuario que introduzca el número y mostrar por pantalla si es primo o no.

numero = int(input("Introduzca un número entero positivo: "))

# Si el número es menor que 2, no es primo
if numero < 2:
    print(numero, "no es un número primo")
else:
    # Se comprueba si el número es divisible por algún número del 2 al 1
    for i in range(2, numero):
        if numero % i == 0:
            # Si el número es divisible, no es primo
            print(numero, "no es un número primo")
            break
    else:
        # Si el bucle no se rompió, entonces el número es primo
        print(numero, "es un número primo")

# Implementa un algoritmo que resuelva el siguiente problema: dado un número entero positivo n, se debe encontrar el número más grande que se puede formar utilizando los dígitos de n. Por ejemplo, si n = 67394, el número más grande que se puede formar es 97643. El algoritmo debe pedir al usuario que introduzca el número n y mostrar el resultado por pantalla.

n = input("Introduce varios numeros enteros: ")
print(f"n = {n}")
numeros = sorted(n, reverse = True) #La función "sorted()" en Python se utiliza para ordenar una secuencia

#El método join() en Python es utilizado para unir una secuencia de elementos en una cadena.
separador = ""
orden = separador.join(numeros)
print(f"El número más grande que se puede formar es: {orden}")


