#Solicita un número N y muestra todos los números
#primos desde 2 hasta N. Para cada número, verifica si
#es divisible entre 2 y hasta su raíz cuadrada.

n = int(input("Ingrese el número N: "))

for numero in range(2, n + 1):
    es_primo = True
    for divisor in range(2, numero):
        if numero % divisor == 0:
            es_primo = False
    if es_primo:
        print(numero, "es primo")