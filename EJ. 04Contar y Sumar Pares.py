contador = 0 
suma = 0

for i in range(1, 21):
    if i % 2 == 0:
        contador += 1
        suma += i

print("Cantidad de numeros pares del 1 al 20:", contador)
print("Suma de numeros pares del 1 al 20:", suma)