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

""" Crear una función recursiva en Python que reciba un número entero positivo en base decimal y
devuelva su representación en binario como una cadena de texto."""

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

""" Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y 
devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión."""

# n = int(input("Ingrese un número entero positivo para calcular la suma de sus dígitos: "))

# def suma_digitos(n):
#     if n < 10: # Caso base, si el número es de un sólo digito lo retorna
#         return n
#     else:
#         return (n % 10) + suma_digitos(n//10) # Recursión, al número le calcula su última cifra dividiendolo por 10 y luego calcula la suma_digitos con el número sin ese último dígito

# print(f"La suma de los dígitos de {n} es: {suma_digitos(n)}")

"""--------------------------------------------------------"""

# Ejercicio 7: 

"""Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente 
nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva 
el total de bloques que necesita para construir toda la pirámide."""

# n = int(input("Ingrese la cantidad de bloques de la base: "))
# def contar_bloques(n):
#     if n == 0: # Caso base, si me quedo sin bloques devuelve 0
#         return n
#     else:
#         return n + contar_bloques(n-1) # Recursión, por cada valor le sumo el resto menos 1, de esta forma voy usando un ladrillo menos por cada nivel.

# print(f"La cantidad de bloques que se necesitan para completar la pirámide es: {contar_bloques(n)}")

"""--------------------------------------------------------"""

# Ejercicio 8:

"""Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y 
un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número."""

# n = int(input("Ingrese un número entero positivo: "))
# digito = int(input("Ingrese el dígito (0 a 9) que desea contar: "))

# def contar_digito(n, digito):
#     if n == 0: # Caso base, el número no tiene más dígitos
#         return 0 
#     else:
#         ultimo = n % 10 # Valúo el último dígito del número
#         contador = 1 if ultimo == digito else 0  # Si el último dígito es igual al buscado, suma 1, sino suma 0
#         return contador + contar_digito(n // 10, digito) # Recursión se elimina el último dígito (n // 10) y se vuelve a llamar

# print(f"La cantidad de veces que {digito} aparece en {n} es: {contar_digito(n, digito)}")
