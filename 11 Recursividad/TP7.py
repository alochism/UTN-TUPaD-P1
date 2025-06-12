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

"""Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
Posteriormente, muestra la serie completa hasta la posición que el usuario especifique."""

# Fibonacci = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55


from fibonacci import ffibonacci

p = int(input("Ingrese la posición de Fibonacci cuyo valor quiere conocer: "))

while p < 0:
    print ("Error, ingrese un número positivo: ")

print (f"En la posición {p}, el valor de la serie de Fibonacci es:  {ffibonacci(p)}")

