
# Solicita N notas al usuario. Calcula el promedio, la
# nota más alta, la más baja y cuántos estudiantes
# aprobaron (nota >= 11). 
nota = int(input("Ingrese el número de notas: "))
lista_notas=[]
while True:
    for i in range(nota):
        nota=float(input("ingrese su nota :"))
        lista_notas.append(nota)
    break

promedio=sum(lista_notas)/nota
nota_alta= max(lista_notas)
nota_baja=min(lista_notas)
aprobados=len([n for n in lista_notas if n >= 11])
print("el promedio de las notas es : ", promedio)
print("la nota mas alta es : ", nota_alta)
print("la nota mas baja es : ", nota_baja)
print("la cantidad de estudiantes aprobados son : ", aprobados)

