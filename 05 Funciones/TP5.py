"""Práctico 2: Funciones en Python"""

""" 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal."""

# # Creo la función que imprime Hola Mundo
# def imprimir_hola_mundo():
#     print("Hola Mundo!")

# #Programa Principal, aquí ejecuto esa función para que imprima el mensaje
# imprimir_hola_mundo()

#----------------------------------

""" 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), 
deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario"""

# #Creo la función que imprime el saludo con un parámetro que hay que proveer
# def saludar_usuario(nombre):
#     print(f"Hola {nombre}!")

# #Programa principal
# #Solicito que el usuario indique su nombre
# a = input("Por favor indique su nombre: ")
# #Ejecuto la función de saludo utilizando el argumento ingresado por el usuario
# saludar_usuario(a)

#----------------------------------

"""3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en 
[residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados."""

# #Creo la función solicitada con los parámetros indicados
# def informacion_personal(nombre, apellido, edad, residencia):
#     print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# #Programa principal
# #Solicito los argumentos al usuario que luego se utilizarán como parámetros en la función informacion_personal
# nombre = input("Por favor ingrese su nombre: ")
# apellido = input("Por favor ingrese su apellido: ")
# edad = int(input("Por favor ingrese su edad: "))
# residencia = input("Por favor ingrese su residencia: ")
# informacion_personal(nombre, apellido, edad, residencia)

#----------------------------------

""" 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_ circulo(radio) que reciba el radio como 
parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados."""

# #Importo la constante pi que usaré para calcular el área y perímetro del círculo
# from math import pi

# #Funciones auxiliares
# #Creo la función que recibe el radio y devuelve el área
# def calcular_area_circulo(radio):
#     return pi * (radio**2)

# #Creo la función que recibe el radio y devuelve el perímetro
# def calcular_perimetro_circulo(radio):
#     return 2 * pi * radio

# #Programa principal
# # Solicito al usuario el radio del círculo, calculo el área y el perímetro usando las funciones creadas
# radio = float(input("Ingrese el radio del círculo: "))
# area = calcular_area_circulo(radio)
# perimetro = calcular_perimetro_circulo(radio)

# # Muestro los resultados por pantalla.
# print(f"El área del círculo de radio {radio} es: {area}")
# print(f"El perímetro del círculo de radio {radio} es: {perimetro}")

#----------------------------------

""" 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los 
segundos y mostrar el resultado usando esta función."""

# #Creo la función que convierte segundos a horas
# def segundos_a_horas(dato):
#     #Solicito que el resultado en horas quede expresado con cuatro decimales, buscando mayor precisión
#     return round(dato / 3600, 4)

# #Programa principal
# #Se solicita al usuario una cantidad de segundos y se muestra el resultando usando la función propuesta
# seg = float(input("Ingresar una cantidad de segundos: "))

# hora = segundos_a_horas(seg)

# print(f"Los {seg} segundos ingresados equivalen a {hora} horas")

#----------------------------------

"""6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y 
llamar a la función."""

# #Creo la función que generará la tabla de multiplicar del 1 al 10 de un número y lo imprimirá 

# def tabla_multiplicar(dato):
#     #Como quiero recorrer la multiplicación del número del 1 al 10 utilizo for
#     for m in range (1, 11):
#         multiplicacion = dato * m
#         print(f"{dato} x {m} = {multiplicacion}")

# #Programa principal
# #Se solicita un número por consola y se llama a la función tabla_multiplicar(numero) para que muestre la tabla de multiplicar y la imprima.
# num = float(input("Ingrese un número: "))

# tabla_multiplicar(num)

#----------------------------------

""" 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. 
Mostrar los resultados de forma clara."""

# #Creo la función que realizará las operaciones matemáticas solicitadas, 
# def operaciones_basicas(a, b):
#     return (a + b), (a - b), (a * b), (a / b)

# #Programa principal
# #Solicito los dos valores por consola (a, b) con los cuales generaré las tuplas con las operaciones matemáticas solicitadas
# a = float(input("Ingrese un primer número: "))
# b = float(input("Ingrese un segundo número: "))
# #Valido que b sea distinto de 0, en caso que sea igual indico el error y solicito que ingrese un número válido
# while b == 0:
#     print("No es posible dividir por 0, elija otro número")
#     b = float(input("Ingrese un segundo número: "))

# #Con los valores validados genero las variables con las operaciones de la función operaciones_basicas
# suma, resta, multiplicacion, division = operaciones_basicas(a, b)

# print(f"\nResultado de las operaciones entre {a} y {b}:")
# print(f"Suma --> ({a} + {b}) = {suma}")
# print(f"Resta --> ({a} - {b}) = {resta}")
# print(f"Multiplicación --> ({a} x {b}) = {multiplicacion}")
# print(f"División --> ({a} / {b}) = {division}")

#----------------------------------

""" 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los 
datos y llamar a la función para mostrar el resultado con dos decimales."""

# #Creo la función calcular_imc(peso, altura)
# def calcular_imc(peso, altura):
#     #El valor debe ser devuelto con dos dígitos decimales, por eso uso round(valor, cantidad de decimales)
#     return round(peso / (altura**2), 2)

# #Programa principal
# #Aquí solicito los valores de peso en kg y altura en metros, llamo a la función calcular_imc e imprimo el resultado
# peso = float(input("Ingrese su peso en kilogramos: "))
# altura = float(input("Ingrese su altura en metros: "))
# #Valido que no se ingresen valores incorrectos
# while peso <= 0 or altura <= 0:
#     print("Error, los datos no pueden ser 0 ni negativos")
#     peso = float(input("Ingrese su peso en kilogramos: "))
#     altura = float(input("Ingrese su altura en metros: "))

# imc = calcular_imc(peso, altura)
# print(f"El Índice de Masa Corporal es: {imc}")

#----------------------------------

""" 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en 
Celsius y mostrar el resultado usando la función"""






