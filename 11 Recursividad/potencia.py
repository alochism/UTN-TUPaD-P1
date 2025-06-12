"""Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, 
utilizando la fórmula 𝑛𝑚= 𝑛∗𝑛(𝑚−1). Prueba esta función en un algoritmo general."""

def potencia(n,m):
    if m == 0: # Caso base
        return 1
    else:
        return n * potencia(n,m-1) # Recursión, multiplica n una cantidad m de veces
    
if __name__=="__main__":
    n=10
    m=5
    print(potencia(n,m))