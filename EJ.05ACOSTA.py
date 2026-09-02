a = float(input("Ingrese el primer numero: "))
b = float(input("Ingrese el segundo numero: "))
op = input("Ingrese la operacion (+, -, *, /): ")

if op == "+":
    print("Resultado:", a + b)
elif op == "-":
    print("Resultado:", a - b)
elif op == "*":
    print("Resultado:", a * b)
elif op == "/":
    if b == 0:
        print("No se puede dividir entre cero")
    else:
        print("Resultado:", a / b)
else:
    print("Operacion no valida")
