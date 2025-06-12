"""Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. 
Posteriormente, muestra la serie completa hasta la posición que el usuario especifique."""

# Fibonacci = 1, 1, 2, 3, 5, 8, 13, 21, 34, 55

def ffibonacci(num): 
    if num == 0 or num == 1: # Caso base
        return 1
    else:
        return ffibonacci(num-1) + ffibonacci(num-2) # Recursión

if __name__=="__main__":
    num = 4
    print (ffibonacci(num))

