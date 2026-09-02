n = int(input("Cuántas notas: "))
notas = [float(input(f"Nota {i+1}: ")) for i in range(n)]

promedio = sum(notas) / len(notas)
aprobados = sum(1 for nota in notas if nota >= 11)

print("Promedio:", promedio)
print("Más alta:", max(notas))
print("Más baja:", min(notas))
print("Aprobados:", aprobados)