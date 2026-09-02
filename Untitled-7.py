
# Genera un número aleatorio entre 1 y 100. El usuario
# debe adivinarlo. En cada intento, indica si el número
# secreto es mayor o menor. Cuenta los intentos

import random
ramdom_number = random.randint(1, 100)
intentos = 0
while True:
    numero=int(input("ingrese su numero :"))
    if numero < 1 or numero >100:
        print ("el numero ingresado no es valido, ingrese un numero entre 1 y 100")
    else:
        intentos+=1
        if numero <ramdom_number:
            print(" el numero es mayor : ", numero)
        elif numero > ramdom_number:
            print(" El numero es menor . ", numero)
        else:
            print(" Felicidades, adivinaste el numero en ", intentos, "intentos")
            break
    
