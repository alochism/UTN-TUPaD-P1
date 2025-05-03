""" Práctico 5: Listas """

""" 1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range. """

# #Creo la lista usando range, indicando que recorra de vaya de 1 a 100 y verifique si el número es divisible por 4, si lo es lo suma al final de la lista

# lista=[]
# for i in range (1, 101):
#     if i % 4 == 0:
#         lista.append(i)
        
# print (lista)

# #Otra forma usando list y range
# #Creo una lista indicando que vaya de 4 al 100, de 4 en 4
# lista2 = list(range(4, 101, 4)) 
# print (lista2)


""" 2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien 
investigar cómo funciona el indexing con números negativos! """

# #Armo la lista de 5 elementos
# lista=["Ford", "Chevrolet", "VW", "BMW", "Peugeot"]

# #Creo la variable que extrae el penúltimo elemento, -1 es el último entonces -2 será el penúltimo
# mostrar_penultimo = lista[-2]

# #Imprimo el elemento solicitado
# print(f"El penúltimo elemento de la lista es {mostrar_penultimo}")


"""3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar 
los corchetes sin nada en su interior. Por ejemplo: lista_vacia = []"""

# #Creo la lista vacía
# lista=[]

# #Agrego tres elementos
# lista.append("Primero")
# lista.append("Segundo")
# lista.append("Tercero")

# #Finalmente muestro la lista final con los 3 elementos
# print(lista)


""" 4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. 
¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos! animales = ["perro", "gato", "conejo", "pez"]"""

# #Creo la lista animales
# animales = ["perro", "gato", "conejo", "pez"]
# print (f"\nLista Animales = : {animales}\n")

# #Busco reemplazar el segundo y último elemnto por los indicados en la consigna
# animales[1]="loro"
# animales[-1]="oso"

# #Imprimo la lista modificada
# print(f"Luego de la modificación del segundo y último elemento")
# print(f"\nLista Animales: {animales}\n")


""" 5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza. """

# numeros = [8, 15, 3, 22, 7]
# numeros.remove(max(numeros))
# print(numeros)

# #RESPUESTA --> Muestra: [8, 15, 3, 7] Se removió el elemento 22, es decir, lo que hace el programa es eliminar el máximo valor de la lista dada.


""" 6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros."""
# #Creo la lista del 10 al 30 incluídos, con salto de 5 en 5, utilizando range
# lista=list(range(10,31,5))

# #Imprimo los dos primeros valores
# print(lista[:2])


""" 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera. autos = ["sedan", "polo", "suran", "gol"]"""

# #Creo la lista autos
# autos = ["sedan", "polo", "suran", "gol"]

# #Reemplazo los dos valores centrales
# autos[1:3]=["kuga", "focus"]

# #Imprimo la nueva lista
# print(autos)


""" 9) Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla"""

# #Creo la lista compras
# compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
# #La muestro como referencia
# print(f"\nLa lista original es: {compras}")

# # a) Agrego jugo a la lista del tercer cliente usando append
# compras[2].append("jugo")
# #Compruebo si se sumó correctamente
# print(f"\nLuego de sumar jugo al tercer cliente: {compras}\n")

# # b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
# compras[1][1]="tallarines"

# #Compruebo si se reemplazó correctamente
# print(f"Luego de reemplazar fideos por tallarines del segundo cliente: {compras}\n")

# # c) Eliminar "pan" de la lista del primer cliente.
# compras[0].remove("pan")

# #Compruebo si se eliminó correctamente
# print(f"Luego de eliminar pan del primer cliente: {compras}\n")

# #Finalmente la lista final
# print(f"Compra final: {compras}\n")


""" 10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla."""

# #Creo la lista anidada
# lista_anidada=[15, True, [25.5, 57.9, 30.6], False]

# #Imprimo cada uno de los valores para comprobar que cumple con la consigna
# print(f"\n{lista_anidada[0]}\n")
# print(f"{lista_anidada[1]}\n")
# print(f"{lista_anidada[2][0]}\n")
# print(f"{lista_anidada[2][1]}\n")
# print(f"{lista_anidada[2][2]}\n")
# print(f"{lista_anidada[3]}\n")

# #Finalmente imprimo la lista completa
# print(f"{lista_anidada}\n")
