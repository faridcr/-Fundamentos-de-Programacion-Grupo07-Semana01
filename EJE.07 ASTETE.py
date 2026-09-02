import random

numero_secreto = random.randint(1, 100)
intentos = 0

while True:
    intento = int(input("Adivina el número (1-100): "))
    intentos += 1

    if intento < numero_secreto:
        print("El número secreto es mayor")
    elif intento > numero_secreto:
        print("El número secreto es menor")
    else:
        print("¡Correcto! Lo adivinaste en", intentos, "intentos")
        break