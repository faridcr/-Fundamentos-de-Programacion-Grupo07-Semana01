import random

secreto = random.randint(1, 100)
intentos = 0

while True:
    numero = int(input("Adivina el numero: "))
    intentos = intentos + 1

    if numero < secreto:
        print("El numero secreto es mayor")
    elif numero > secreto:
        print("El numero secreto es menor")
    else:
        print("Correcto")
        print("Intentos:", intentos)
        break
