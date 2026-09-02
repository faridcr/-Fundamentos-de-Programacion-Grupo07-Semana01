num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

operador = input("Ingrese el operador (+, -, *, /): ")

if operador == "+": 
    resultado = num1 + num2
    print("El resultado de la suma es:", resultado)

elif operador == "-":
    resultado = num1 - num2
    print("El resultado de la resta es:", resultado)

elif operador == "*":
    resultado = num1 * num2
    print("El resultado de la multiplicación es:", resultado)

elif operador == "/":
    if num2 != 0:
        resultado = num1 / num2
        print("El resultado de la división es:", resultado)
    else:
        print("Error: No se puede dividir entre cero.")

else:
    print("Error: Operador no válido")

