#Solicita N notas al usuario. Calcula el promedio, la
#nota más alta, la más baja y cuántos estudiantes
#aprobaron (nota >= 11). Muestra estadísticas
#completas.

n = int(input("¿Cuántas notas ingresará?: "))

suma = 0
mayor = 0
menor = 20
aprobados = 0

for i in range(n):
    nota = float(input("Ingrese la nota: "))
    suma = suma + nota

    if nota > mayor:
        mayor = nota
    if nota < menor:
        menor = nota
    if nota >= 11:
        aprobados = aprobados + 1

promedio = suma / n

print("Promedio:", promedio)
print("Nota más alta:", mayor)
print("Nota más baja:", menor)
print("Estudiantes aprobados:", aprobados)