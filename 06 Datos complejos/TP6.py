"""TP 6 - Estructuras de datos complejas"""

"""Objetivo: Dominar el uso de estructuras de datos complejas en Python para almacenar, organizar y manipular 
datos de manera eficiente, aplicando buenas prácticas y optimizando el rendimiento de las aplicaciones."""

""" 1) Dado el diccionario precios_fruta, añadir las siguientes frutas"""

# precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# # Agregamos nuevas frutas

# precios_frutas['Naranja'] = 1200
# precios_frutas['Manzana'] = 1500
# precios_frutas['Pera'] = 2300

# print(precios_frutas)


"""-----------------------------------------------"""

""" 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el 
punto anterior, actualizar los precios de las siguientes frutas:"""

# precios_frutas['Banana'] = 1330
# precios_frutas['Manzana'] = 1700
# precios_frutas['Melón'] = 2800

# print(precios_frutas)

"""-----------------------------------------------"""

""" 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el 
punto anterior, crear una lista que contenga únicamente las frutas sin los precios."""

# solo_frutas = list(precios_frutas.keys())

# print(solo_frutas)

"""-----------------------------------------------"""

""" 4) Escribí un programa que permita almacenar y consultar números telefónicos."""


# tel = {}

# # Cargamos 5 contactos

# for i in range(3):

#     nombre = input("Ingrese nombre del contacto: ")
#     num = input("Ingrese número de teléfono: ")
#     tel[nombre] = num

# # Consultamos un contacto

# consulta = input("Ingrese el nombre para consultar su número: ")
# if consulta in tel:
#     print("El número es:", tel[consulta])
# else:
#     print("Contacto inexistente.")

"""-----------------------------------------------"""


""" 5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra."""

# frase = input("Ingrese frase: ")

# palabras = frase.split()

# # Set de palabras únicas

# palabras_unicas = set(palabras)
# print("Palabras únicas:", palabras_unicas)

# # Diccionario con cantidad de repeticiones

# conteo = {}
# for palabra in palabras:
#     conteo[palabra] = conteo.get(palabra, 0) + 1

# print("Cantidad de cada palabra:", conteo)

"""-----------------------------------------------"""

""" 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno."""

# alumnos = {}

# for i in range(3):
#     nombre = input("Nombre del alumno: ")
#     nota1 = float(input("Nota 1: "))
#     nota2 = float(input("Nota 2: "))
#     nota3 = float(input("Nota 3: "))
#     alumnos[nombre] = (nota1, nota2, nota3)

# for nombre, notas in alumnos.items():
#     promedio = sum(notas) / 3
#     print(f"Alumno: {nombre} - Promedio: {promedio}")

"""-----------------------------------------------"""

""" 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)."""

# aprobados_p1 = {1, 2, 3, 4, 5}
# aprobados_p2 = {3, 4, 5, 6, 7}

# print("Aprobaron 2 parciales:", aprobados_p1 & aprobados_p2)
# print("Aprobaron 1 parcial:", (aprobados_p1 ^ aprobados_p2))
# print("Aprobaron al menos uno:", aprobados_p1 | aprobados_p2)

"""-----------------------------------------------"""

"""8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe."""

# stock = {"jabon":5, "detergente":4, "shampoo":6}

# producto = input("Producto a consultar: ")

# if producto in stock:
#     print(f"Stock de {producto}: {stock[producto]}")
#     agregar = int(input("¿Cuántas unidades se agregarán?: "))
#     stock[producto] += agregar
# else:
#     nuevo_stock = int(input("Producto nuevo. Ingresar stock: "))
#     stock[producto] = nuevo_stock

# print("Stock actualizado:", stock)

"""-----------------------------------------------"""

""" 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Ejemplo:"""

# agenda = {}

# # Ejemplo de carga

# agenda[(4, 8)] = "Cumpleaños Juan"
# agenda[(9, 13)] = "Reunión"
# agenda[(15, 16)] = "Turno médico"

# dia = int(input("Día a consultar: "))
# hora = int(input("Hora a consultar: "))

# if (dia, hora) in agenda:
#     print("Actividad:", agenda[(dia, hora)])
# else:
#     print("No hay eventos.")

"""-----------------------------------------------"""

"""10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores."""

# paises = {
#     'Argentina': 'Buenos Aires',
#     'Brasil': 'Brasilia',
#     'Italia': 'Roma',
#     'Rusia': 'Moscú'
# }

# capitales = {}

# for pais, capital in paises.items():
#     capitales[capital] = pais

# print("Dicc invertido:", capitales)
