
# Escribe un programa que solicite la base y
# altura de un rectángulo y calcule su área (A =
# base × altura) y su perímetro (P =
# 2×(base+altura)). Muestra los resultados
# formateados

base=float(input("ingrese la medida de la base del rectangulo: "))
altura=float(input("ingrese la medida de la altura del rectangulo: "))

area=base*altura
perimetro=2*(base+altura)

print(f"El área del rectángulo es: {area}")
print(f"El perímetro del rectángulo es: {perimetro}")