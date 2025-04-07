"""Práctico 3: Estructuras condicionales"""

""" 1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”."""

# edad = int(input("Ingrese su edad: "))
# if edad > 18:
#     print("Es mayor de edad.")
# else:
#     print("NO es mayor de edad.")

#-----------------------------------------

""" 2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; 
en caso contrario deberá mostrar el mensaje “Desaprobado”."""

# nota = float(input("Ingrese su nota: "))
# if nota >= 6:
#     print("Aprobado")
# else:
#     print("Desaprobado")

#-----------------------------------------

"""3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; 
en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar."""

# num = int(input("Ingrese un número: "))
# if num % 2 == 0:
#     print("Ha ingresado un número par.")
# else:
#     print("Por favor, ingrese un número par.")

#-----------------------------------------

""" 4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: mayor o igual que 12 años 
y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años."""

# edad = int(input("Por favor ingrese su edad: "))
# if edad < 12:
#     print("Pertenece a la categoría Niño/a.")
# elif edad >= 12 and edad < 18:
#     print("Pertenece a la categoría Adolescente.")
# elif edad >= 18 and edad < 30:
#     print("Pertenece a la categoría Adulto/joven.")
# else:
#     print("Pertenece a la categoría Adulto/a.")

#-----------------------------------------

""" 5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, 
imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". 
Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string."""
# La función len() devuelve la cantidad de caracteres de un string (o elementos de una lista).

# codigo = input("Por favor ingrese una contraseña de entre 8 y 14 caracteres: ")
# if len(codigo) >= 8 and len(codigo) <= 14:
#     print("Ha introducido una contraseña correcta.")
# else:
#     print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#-----------------------------------------

""" 6) El paquete statistics de python contiene funciones que permiten tomar una lista de números y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el 
siguiente: from statistics import mode, median, mean mi_lista = [1,2,5,5,3] mean(mi_lista) En la documentación oficial se puede encontrar más información sobre este paquete: 
https://docs.python.org/es/3.8/library/statistics.html. La moda (mode), la mediana (median) y la media (mean) son parámetros estadísticos que se pueden utilizar para predecir la forma de una
distribución normal a partir del siguiente criterio: ● Sesgo positivo o a la derecha: cuando la media es mayor que la mediana y, a su vez, la mediana es mayor que la moda. ● Sesgo negativo o 
a la izquierda: cuando la media es menor que la mediana y, a su vez, la mediana es menor que la moda. ● Sin sesgo: cuando la media, la mediana y la moda son iguales.
Teniendo en cuenta lo antes mencionado, escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, 
negativo o no hay sesgo. Imprimir el resultado por pantalla.
Definir la lista numeros_aleatorios de la siguiente forma: import random numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
Nota: el bloque de código anterior crea una lista con 50 números entre 1 y 100 elegidos de forma aleatoria."""

# from statistics import mode, median, mean #moda=mode, mediana=median, media=mean
# import random

# numeros_aleatorios = [random.randint(1, 100) for i in range (50)]

# media = mean(numeros_aleatorios)
# mediana = median(numeros_aleatorios)
# moda = mode(numeros_aleatorios)

# print("Números: ", numeros_aleatorios)
# print("La media es: ", media)
# print("La mediana es: ", mediana)
# print("La moda es: ", moda)

# if media > mediana and mediana > moda:
#     print("Sesgo positivo a la derecha")
# elif media < mediana and mediana < moda:
#     print("Sesgo negativo a la izquierda")
# elif media == mediana and mediana == moda:
#     print("Sin sesgo")
# else:
#     print("Nada de lo anterior se cumple")

#-----------------------------------------

""" 7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla."""

# #Solicito al usuario que ingrese una palabre o frase por pantalla
# frase = (input("Ingrese una palabra o frase: ")) #no hace falta hacer str(input(frase)) ya que por defecto el input siempre devuelve un string

# #Con la frase ingresada, solicit que la última letra pertenezca al conjunto de vocales "aeiou". Como el conjunto es en minúsculas y Python discrimina minúsculas y mayúsculas, hagtransformo la
# # última letra a minúscula con lower(). 
# if frase[-1].lower() in "aeiou":
#     print(frase + "!") 
# # En caso que la última letra no sea una vocal, se imprime la frase como se escribió por consola
# else:
#     print(frase) 

#-----------------------------------------

""" 8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el usuario e imprimir el resultado por pantalla. Nota: 
investigue uso de las funciones upper(), lower() y title() de Python para convertir entre mayúsculas y minúsculas."""

# nombre = input("Ingrese su nombre: ")
# opcion = int(input("Ingrese la opción 1 si quiere todo su nombre en MAYÚSCULAS, la opción 2 si prefiere en minúsculas y la opción 3 si quiere sólo la primer letra MAYÚSCULA: "))
# if opcion == 1:
#     print(nombre.upper())
# elif opcion == 2:
#     print(nombre.lower())
# elif opcion == 3:
#     print(nombre.title())
# else:
#     print("No ha elegido una opción válida.")

#-----------------------------------------

"""9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala)."""

# magnitud = float(input("Ingrese la magnitud del terremoto para valuarlo en la escala de Richter: ")) #Solicito por consola la magnitud del terremoto, uso float ya que las magnitudes pueden tener valores decimales.

# if magnitud < 3: #Uso las distintas estructuras condicionales para que se vayan imprimiendo distintos mensajes de acuerdo a la magnitud ingresada. 
#     print(f"El terremoto de magnitud {magnitud} es: Muy leve")
# elif magnitud >= 3 and magnitud < 4:
#     print(f"El terremoto de magnitud {magnitud} es: Leve")
# elif magnitud >= 4 and magnitud < 5:
#     print(f"El terremoto de magnitud {magnitud} es: Moderado")
# elif magnitud >= 5 and magnitud < 6:
#     print(f"El terremoto de magnitud {magnitud} es: Fuerte")
# elif magnitud >= 6 and magnitud < 7:
#     print(f"El terremoto de magnitud {magnitud} es: Muy Fuerte")
# else:
#     print(f"El terremoto de magnitud {magnitud} es: Extremo")

#-----------------------------------------

"""10) Utilizando la información aportada en la siguiente tabla sobre las estaciones del año.
Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
si el usuario se encuentra en otoño, invierno, primavera o verano."""

hemisferio = input("Indique en que hemisferio se encuentra, `S` para hemisferio Sur y `N` para hemisferio Norte: ") #Solicito que se ingrese por consola los tres datos solicitados, hemisferio, mes y día.
mes = int(input("Indique en que mes del año se encuentra (1 - 12): "))
dia = int(input("Indique en que día del año se encuentra (1 - 31): "))
hemisferio.upper() #En caso que se ingrese el hemisferio en minúscula, de esta forma aseguro que al analizar la variable, se encuentre en mayúsculas
hemisferio = hemisferio.upper()

if dia > 31: #Condiciono que el día indicado sea a lo sumo 31 ya que ningún mes tiene mas días. A su vez condiciono que si es Febrero, se ingrese a lo sumo el día 29. No se tienen en cuenta los años bisiestos.
    print("Los meses del año tienen como máximo 31 días, indique una fecha correcta.")
if mes == 2 and dia > 29:
    print("El mes de febrero sólo tiene 29 días, indique una fecha correcta.")

#Verano/Invierno
else:
    if (mes == 12 and dia >=21) or (mes in [1,2]) or (mes == 3 and dia <=20): #Uso las distintas estructuras condicionales para que se vayan guardando las distintas estaciones dependiendo del hemisferio y la fecha.
        if hemisferio == "S":
            estacion = "Verano"
        else:
            estacion = "Invierno"
#Otoño/Primavera
    elif (mes == 3 and dia >=21) or (mes in [4,5]) or (mes == 6 and dia <=20):
        if hemisferio == "S":
            estacion = "Otoño"
        else:
            estacion = "Primavera"
#Invierno/Verano
    elif (mes == 6 and dia >=21) or (mes in [7,8]) or (mes == 9 and dia <=20):
        if hemisferio == "S":
            estacion = "Invierno"
        else:
            estacion = "Verano"
#Primavera/Otoño
    elif (mes == 9 and dia >=21) or (mes in [10,11])or (mes == 12 and dia <=20):
        if hemisferio == "S":
            estacion = "Primavera"
        else:
            estacion = "Otoño"

print(f"Siendo {dia}/{mes} y encontrandose en el hemisferio {hemisferio}, la estación es {estacion}")



