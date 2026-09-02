
# Solicita dos números y un operador (+, -, *, /). Usa una estructura
# Según para determinar la operación. Maneja el caso de división por
# cero con una condicional

n1=int(input("ingrese el primer numero :"))
n2=int(input("ingrese el segundo numero :"))
operador=input("ingrese un operador (+,-,*,/,:)")

while operador not in ["+","-","*","/"]:
    print("escoja un operador valido ")
    operador=input("ingrese un operador valido (+,-,*,/,:)")

if operador=="+":
    suma=n1+n2
    print("el resulatado de la suma es : ", suma)
elif operador=="-":
    resta=n1-n2
    print("el resulatado de la resta es :", resta)
elif operador=="*":
    multi=n1*n2
    print("el resultado de la multiplicacion es :", multi)
elif operador=="/":
    while n2==0:
        print("no se puede dividir entre 0")
        n2=int(input("ingrese un  numero que no sea 0 : "))
    else:
        divi=n1/n2
        print("el resultado de la division es :", divi)
