cantidad = 0
suma = 0

for i in range(1, 21):
    if i % 2 == 0:
        cantidad = cantidad + 1
        suma = suma + i

print("Cantidad de pares:", cantidad)
print("Suma de los pares:", suma)
