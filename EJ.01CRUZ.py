# Escribe un programa que solicite la base y
# altura de un rectángulo y calcule su área (A =
# base × altura) y su perímetro (P =
# 2×(base+altura)). Muestra los resultados
# formateados.

base = float(input("Ingrese la base: "))
altura = float(input("Ingrese la altura: "))

area = base * altura
perimetro = 2 * (base + altura)

print("El área es:", area)
print("El perímetro es:", perimetro)