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

# #Importo random para poder solicitar un número aleatorio entre 0 y 9.
# import random

# #Empiezo el contador en 0
# cont = 0

# #Solicito por consola un número del 0 al 9 
# adivina = int(input("Por favor ingrese un número entero entre 0 y 9 para descubrir el número misterioso: "))

# #Al ingresar el primer número el contador aumenta en 1, esto ocurrirá siempre ya que debo utilizar un primer intento para empezar el juego
# cont += 1

# #Genero el número aleatorio
# num = random.randint(0, 9)

# #Si el número ingresado por consola es incorrecto, ingreso al bucle, donde indico cuántos intentos se han realizado, solicito que se ingrese otro número y sumo el contador en 1 cada vez
# while adivina != num:
#     print(f"Ha realizado {cont} intentos.")
#     adivina = int(input("Ingrese otro número:"))
#     cont += 1

# #Si el número ingresado es correcto, entonces salgo del bucle y termino el juego indicando cuál es el número correcto y cuantos intentos se necesesitaron para descubirlo.
# else:
#     print(f"CORRECTO! el número miesterioso es {num}, lo descubriste en {cont} intentos!")

#-----------------------------------------

""" 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente."""

# #Como sé cual es el rango de iteraciones que necesito, uso for. Sabiendo que toma el valor inicial pero no el final, indico que vaya de 101 a 0 (recorrerá de 101 a 1), con paso -2 en 
# # cada iteración, si bien empiezo la iteración en un número impar y restando 2 seguirá siendo un número impar, eso se corrige en la linea de código siguiente, donde muestro 
# # el valor de x restando 1, de esta forma llevando el valor de número impar a uno par.
# for x in range(101, 0, -2):

# #Luego le pido que imprima x-1, de esta manera si bien recorre de 101 a 1, mostrará el resultado de 100 a 0, separando con + cada iteración, sin hacer salto de línea
#     print(x-1, end= " + ")

#-----------------------------------------

""" 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario."""
# #Como el enunciado indica los números comprendidos entre 0 y el número ingresado, no tomo en cuenta en la suma a los extremos. Recorro de 0 (neutro en la suma) hasta (número - 1).

# #Solicito se ingrese un número entero positivo por consola
# num = int(input("Ingrese un número entero positivo: "))

# #Inicializo la suma en 0
# suma = 0

# #Valido que el entero ingresado sea positivo
# if num <= 0:
#     print("Error, debe ingresar un número entero positivo.")

# #Validado que el número sea entero positivo, voy a saber la cantidad de iteraciones a realizar, armo el bucle para esas iteraciones, donde se irá modificando 
# # el sumando para que vaya tomando cada valor de enteros entre 0 y el ingresado, y guardando su suma en la variable suma
# else:
#     for x in range(0, num):
#         suma += x

# #Terminado el bucle, imprimo el resultado de la suma, indicando cuantos enteros se sumaron y cuál es el resultado
#     print(f"Entre 0 y {num} hay {num-1} enteros y su suma es {suma}")

#-----------------------------------------

""" 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

# #En vez de 100 utilizo la variable numeros para setear la cantidad de intentos, modificando 5 por 100 funciona para esa cantidad de números
# numeros = 5

# #Inicializo en 0 las variables que luego se irán modificando 
# par = 0
# impar = 0
# pos = 0
# neg = 0

# #Como sé la cantidad de iteraciones que usaré, utilizo for. Donde el rango será numeros, imprimo (x+1) para que imprima de 1 a 5 en vez de 0 a 4, pero la cantidad de iteraciones es la misma 
# for x in range(numeros):
#     num = int(input(f"Ingrese el {x+1}° de {numeros}: "))

# #Por cada valor ingresado se hace la validación sobre si es par, impar, negativo o positivo, sumando en uno las respectivas variables si corresponde
#     if num%2 == 0:
#         par += 1
#     else:
#         impar += 1

#     if num >= 0:
#         pos += 1
#     else:
#         neg += 1

# #Finalmente se imprime el resultado final de los valores obtenidos
# print(f"Se han ingresado {numeros} números, de los cuáles {par} son pares, {impar} son impares, {pos} son positivos y {neg} negativos")

#-----------------------------------------

"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

# #Pruebo con 5 valores, cambiando a 100 la variable funciona como indica el enunciado
# valores = 5

# #Inicializo la suma en 0
# suma = 0

# #Se acalara el tipo de dato que se debe ingresar y qué es lo que hará el programa
# print(f"Se le solicitará que ingrese {valores} valores, los cuales deben ser enteros. Se calculará la media de dichos valores.")

# #Como sé cuantas iteraciones haré, utilizo el for. Por cada iteración ingreso un número, el cual se suma y actualiza la variable suma
# for x in range(valores):
#     num = int(input(f"Ingrese el {x+1}° valor de {valores}: "))
#     suma += num

# #Luego de hacer todas las iteraciones, con el valor final de variable suma y la cantidad de números o iteraciones ingresadas, calculo la media
# media = suma / valores

# #Imprimo el valor obtenido
# print(f"La media de los {valores} valores ingresados es {media}")

#-----------------------------------------

""" 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

# numero = (input("Ingrese un número: ")) #Solicito un número que quedará como string para poder contar la cantida de caracteres

# num = int(numero) #Para poder trabajar con los operadores matemáticos, convierto el número ingresado de string a integer

# valorf = 0 #Inicializo la variable valor final (valorf) en 0, esta me servirá para ir armando número invertido en el bucle

# if num < 0:         #En caso que el número ingresado sea negativo, debo restar un caracter a la cantidad ingresada ya que el signo negativo también se cuenta
#     a = len(numero) - 1         #Contabilizo la cantidad de dígitos que se ingresaron
#     num2 = abs(num)         #Calculo el valor absoluto del número negativo ingresado, lo convierto a positivo para trabajar sin problemas en la suma que armará el valor invertido
#     for x in range (a):         #Calculo cuantas veces tendré que hacer el bucle dependiendo de la cantidad de dígitos del número
#         digito = num2 % 10          #Obtengo el último dígito del número ingresado y lo guardo en la variable digito
#         valorf = valorf * 10 + digito           #La variable valorf se irá actualizando en cada iteración multiplicando por 10 cada vez, de esta forma irá acomodando el último valor al principio y el primero al final, al sumarse al valor de valorf el dígito más grande ira al final, el segundo irá antepenúltimo, y así, invirtiendo el valor del número
#         num2 = num2 // 10           #Se va acutualizando el valor del num2 por cada iteración, descartando el último dígito cada vez, así al llegar a 0 ya no tendrá dígitos para actualizarse la variable digito
#     print(f"El valor invertido es {-1*valorf}")         #Como se calculó el valor positivo, en este caso se imprime la respuesta multiplicando por -1 el valor final obtenido

# else:           #Aquí se realiza el caso en que el número sea positivo, igual que en el caso anterior, sólo que sin restar un dígito al valor ingresado y sin multiplicar por -1 el valor final obtenido
#     a = len(numero)
#     for x in range (a):
#         digito = num % 10
#         valorf = valorf * 10 + digito
#         num = num // 10
#     print(f"El valor invertido es {valorf}")