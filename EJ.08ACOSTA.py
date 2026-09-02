n = int(input("Ingrese la cantidad de notas: "))

suma = 0
aprobados = 0
mayor = 0
menor = 20

for i in range(n):
    nota = float(input("Ingrese la nota: "))
    suma = suma + nota

    if nota >= 11:
        aprobados = aprobados + 1

    if nota > mayor:
        mayor = nota

    if nota < menor:
        menor = nota

promedio = suma / n

print("Promedio:", promedio)
print("Nota mayor:", mayor)
print("Nota menor:", menor)
print("Aprobados:", aprobados)
print("Desaprobados:", n - aprobados)
