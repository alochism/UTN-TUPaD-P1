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

#Importo la constante pi que usaré para calcular el área y perímetro del círculo
from math import pi

#Funciones auxiliares
#Creo la función que recibe el radio y devuelve el área
def calcular_area_circulo(radio):
    return pi * (radio**2)

#Creo la función que recibe el radio y devuelve el perímetro
def calcular_perimetro_circulo(radio):
    return 2 * pi * radio

#Programa principal
# Solicito al usuario el radio del círculo, calculo el área y el perímetro usando las funciones creadas
radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

# Muestro los resultados por pantalla.
print(f"El área del círculo de radio {radio} es: {area}")
print(f"El perímetro del círculo de radio {radio} es: {perimetro}")
