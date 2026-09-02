num1 = float(input("Ingrese el primer número: "))
operador = input("Ingrese el operador (+, -, *, /): ")
num2 = float(input("Ingrese el segundo número: "))

match operador:
    case "+":
        print("Resultado:", num1 + num2)
    case "-":
        print("Resultado:", num1 - num2)
    case "*":
        print("Resultado:", num1 * num2)
    case "/":
        if num2 == 0:
            print("Error: no se puede dividir entre cero")
        else:
            print("Resultado:", num1 / num2)
    case _:
        print("Operador no válido")