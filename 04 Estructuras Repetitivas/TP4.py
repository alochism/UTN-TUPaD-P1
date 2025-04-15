"""Práctico 4: Estructuras repetitivas"""

""" 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

# #Se utiliza la estructura for, indicando el rango de partida 0, el cual está incluído en el recorrido y el de finalización 101 ya que dicho término no está incluido, por lo que llegara 
# # hasta el 100. De manera predeterminada, el for avanzará de uno en uno, de esta manera recorrerá desde 0 hasta 100, de a una unidad por vez.
# for x in range (0,101): 
#     print(x) #A medida que x vaya tomando los distintos valores desde 0 a 100, se solicita que vaya imprimiendo cada uno de estos valores. Al llegar al final del recorrido indicado finalizará.

#-----------------------------------------

""" 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene."""

# num = int(input("Por favor ingrese un número entero: "))            #Solicito por pantalla que se ingrese un número, que debe ser entero, si es decimal o string, se producirá un error.
# original = num          #Al número ingresado lo guardo en una nueva variable que usaré al final al expresar el resultado, esto es necesario ya que en las validaciones se irá modificando el número original ingresado.
# num = abs(num)          #Los números negativos también son enteros, debido a la validación que haré, necesito que el número sea positivo, aquí hago esa conversión en caso de ser negativo.
# cont = 0            #Defino un contador y lo inicializo en 0, el contador será el indicador de dígitos en el número ingresado.
# if num == 0:            #Tengo en cuenta un caso en particular, si se ingresa 0, la cantidad de dígitos es 1 y el programa no entra en el bucle.
#     cont = 1
# else:
#     while num > 0:          #Si el número entero ingresado es distinto de 0, entonces será mayor que 0 (ya lo convertimos en positivo en la línea 16).
#     num = num // 10         #Divido el número ingresado en 10, descartando la parte decimal y registrando sólo la entera, cada vez que hago esto el contador se suma en 1, como se ve en la línea 23.
#     cont += 1 
# print(f"El número {original} tiene {cont} dígitos")         #Finalmente expreso el resultado, la cantidad de dígitos del número original será igual a la cantidad de veces que se divide por 10, siendo el resultado de esa división un número entero mayor que 0.

#-----------------------------------------

""" 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores."""

# import math #Importo la librería de matemática ya que se están solicitando números que pueden ser deciomales y los quiero llevar a el número entero, sin contar la parte decimal.

# print("Por favor ingrese dos números:")
# n1 = float(input()) #Se acepta que ingresen números decimales
# n2 = float(input())

# #Aquí guardo los números originales para el mensaje final
# o1 = n1 
# o2 = n2

# #Tomo el valor entero sin redondeos, sino que ignoro el valor decimal
# n1 = math.floor(n1)
# n2 = math.floor(n2)

# #Inicializo la suma en 0
# suma = 0

# #Calculo el valor mínimo y máximo de los dos números ingresados para poder armar el bucle de suma desde el valor más chico hasta el máximo, al mínimo le sumo 1 ya que sino python lo incluye en la suma de manera predeterminada
# minimo = min(n1, n2) + 1
# maximo = max(n1, n2)

# #Valido que los números no sean iguales, o que disten un entero uno de otro, ya que en estos casos no hay enteros entre ellos para sumar
# if maximo - minimo <= 1:
#     print(f"No existen números enteros entre {o1} y {o2} que puedan sumarse")

# #Realizo la suma entre los enteros que hay entre el mínimo y el máximo, excluyéndolos
# else:
#     for x in range(minimo, maximo):
#         suma += x
#     print(f"El valor de la suma de los enteros entre {o1} y {o2} es: {suma}") 

#-----------------------------------------

""" 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0."""

# #Solicito que se ingrese el primer número por consola
# num = int(input("Por favor ingrese un número entero para ser sumados, 0 para terminar el proceso."))

# #Inicializo la suma en 0
# suma = 0

# #Mientras no se ingrese el valor 0, el programa irá sumando cada número ingresado y solicitará que se ingrese otro número. Las sucesivas sumas se guardarán en "suma"
# while num != 0:
#     suma += num
#     num = int(input("por favor ingrese otro número entero: "))

# #Una vez que se ingresa 0, se sale del bucle while y se indica el valor final de "suma" que será la suma de todos los números ingresados antes del 0.
# print(f"La suma de los números ingresados es: {suma}")

#-----------------------------------------

"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random

adivina = int(input("Por favor ingrese un número entero entre 0 y 9 para descubrir el número misterioso: "))

num = random.randint(0, 9)

if adivina == num:
    cont = 1
else:
    cont = 0
    while adivina != num:
        cont += 1
        print(f"Ha realizado {cont} intentos.")
        adivina = int(input("Ingrese otro número:"))
    else:
        print(f"CORRECTO! el número miesterioso es {num}, lo descubriste en {cont+1} intentos!")





