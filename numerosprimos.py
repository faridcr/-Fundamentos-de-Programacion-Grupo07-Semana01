
# Solicita un número N y muestra todos los números
# primos desde 2 hasta N. Para cada número, verifica si
# es divisible entre 2 y hasta su raíz cuadrada.

import math

N=int(input("ingrese un numero : "))

print ("Los números primos desde 2 hasta", N, "son:")

for num in range(2, N ):
    es_primo = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)