n = int(input("Ingrese N: "))

print("Numeros primos:")

for num in range(2, n + 1):
    primo = True

    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

    if primo:
        print(num, end=" ")
