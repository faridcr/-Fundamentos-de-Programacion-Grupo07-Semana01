#Solicita dos números y un operador (+, -, *, /). Usa una estructura
#Según para determinar la operación. Maneja el caso de división por
#cero con una condicional.

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
operador = input("Ingrese la operación (+, -, *, /): ")

if operador == "+":
    print("Resultado:", num1 + num2)
elif operador == "-":
    print("Resultado:", num1 - num2)
elif operador == "*":
    print("Resultado:", num1 * num2)
elif operador == "/":
    if num2 == 0:
        print("Error: no se puede dividir entre cero")
    else:
        print("Resultado:", num1 / num2)
else:
    print("Operador no válido")