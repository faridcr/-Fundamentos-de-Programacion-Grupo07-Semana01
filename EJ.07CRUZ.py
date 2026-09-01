#Genera un número aleatorio entre 1 y 100. El usuario
#debe adivinarlo. En cada intento, indica si el número
#secreto es mayor o menor. Cuenta los intentos.

import random

secreto = random.randint(1, 100)
intentos = 0
adivinado = False

while not adivinado:
    intento = int(input("Adivina el número (1-100): "))
    intentos = intentos + 1

    if intento < secreto:
        print("El número secreto es mayor")
    elif intento > secreto:
        print("El número secreto es menor")
    else:
        print("¡Adivinaste! Intentos:", intentos)
        adivinado = True