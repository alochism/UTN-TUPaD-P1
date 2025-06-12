""" Práctico 11: Aplicación de la Recursividad """

# Ejercicio 1:

""" Crea una función recursiva que calcule el factorial de un número. 
Luego, utiliza esa función para calcular y mostrar en pantalla el factorial 
de todos los números enteros entre 1 y el número que indique el usuario """


# from func_factorial import func_fact # Se importa la función que calcula factoriales

# n = int(input("Ingrese un número positivo para factoriar: ")) # Solicita por consola que ingrese un número

# while n < 0: # Validación

#     n = int(input("Error, ingrese un número positivo: "))

# print(f"El factorial de {n} es: ", func_fact(n)) 

"""--------------------------------------------------------"""

# Ejercicio 2:

""" Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
Posteriormente, muestra la serie completa hasta la posición que el usuario especifique."""

# Fibonacci = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55


# from fibonacci import ffibonacci

# p = int(input("Ingrese la posición de Fibonacci cuyo valor quiere conocer: "))

# while p < 0:
#     print ("Error, ingrese un número positivo: ")

# print (f"En la posición {p}, el valor de la serie de Fibonacci es:  {ffibonacci(p)}")

"""--------------------------------------------------------"""

# Ejercicio 3:

""" Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general."""

# from potencia import potencia
# print ("Se solicita que ingrese el exponente y base para calcular su resultado: ")
# base = int(input("Base: "))
# exponente = int(input("Exponente: "))

# print (f"La potencia de base {base} y exponente {exponente} es: {potencia(base, exponente)}")

"""--------------------------------------------------------"""

# Ejercicio 4:

""" Crear una función recursiva en Python que reciba un número entero positivo en base decimal
y devuelva su representación en binario como una cadena de texto."""

# n = int(input("Ingrese un número natural para convertirlo en binario: "))
# while n < 0:
#     n = int(input("Error, ingrese un número natural para convertirlo en binario: "))
# def enbinario(n):
#     if n < 2:
#         return str(n)
#     else:
#         return enbinario(n // 2) + str(n % 2)
# print (enbinario(n))

"""--------------------------------------------------------"""

# Ejercicio 5:    

""" Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto 
sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed()."""

# palabra = input("Para analizar si es palíndromo, ingrese una palabra sin espacios ni tildes: ")

# def es_palindromo(palabra): 
#     if len(palabra) <= 1: # Caso base, palabra con uno o ningún caracter
#         return "Es palíndromo"
#     elif palabra[0] != palabra[-1]: # Validación, si el primero y último caracter no son iguales, no es palindromo
#         return "No es palíndromo"
#     else:
#         return es_palindromo(palabra[1:-1]) # Recursión, si son palindromos la primera y última, los saco y analizo el segundo y anteúltimo recursivamente

# print(es_palindromo(palabra))

"""--------------------------------------------------------"""

# Ejercicio 6:  