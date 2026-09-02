n = int(input("Cuantas notas vas a ingresar: "))

suma = 0
mayor = 0
menor = 20 
aprovados = 0

for i in range(1,  n + 1):
    nota = float(input("Ingrese la nota " + str(i) + ": "))

    suma += nota

    if nota > mayor:
        mayor = nota

    if nota < menor:
        menor = nota

    if nota >= 11:
        aprovados += 1

promedio = suma / n

print("Promedio:", promedio)
print("nota mas alta:", mayor)
print("nota mas baja:", menor)
print("alumnos aprobados:", aprovados) 
