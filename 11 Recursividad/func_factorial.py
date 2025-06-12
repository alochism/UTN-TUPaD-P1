# Se crea la función factorial recursiva
""" Crea una función recursiva que calcule el factorial de un número. 
Luego, utiliza esa función para calcular y mostrar en pantalla el factorial 
de todos los números enteros entre 1 y el número que indique el usuario """

def func_fact(num):
    if num == 0: # Caso base
        return 1
    else:   
        return num * func_fact(num - 1) # Recursión
    
if __name__=="__main__":    
    num=5
    print(func_fact(num))