# 4. Lee por teclado números y guárdalos en una lista, el proceso finaliza cuando metamos un
# número negativo. Al finalizar el programa se debe mostrar el máximo de los números
# guardado en la lista y los números pares que formen parte de la lista.
from Ejercicio1 import mayor

def pares(lista):
    pares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    return pares

lista = []

num = int(input("Dime un número"))
while num > 0 :
    lista.append(num)
    num = int(input("Dime un número"))
    
print(lista)
print("El número más grande es " + mayor(lista))
print("Los números pares son " + pares(lista))