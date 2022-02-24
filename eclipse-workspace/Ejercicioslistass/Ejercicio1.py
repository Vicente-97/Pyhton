#1. Crea un programa que genere 1OO números de forma aleatoria y que posteriormente ofrezca
# al usuario la posibilidad de:
# 1. Conocer el mayor de los números
# 2. Conocer el menor de los números
# 3. Obtener la suma de todos los números
# 4. Obtener la media de ellos números
# 5. Sustituir el valor de un elemento por otro número introducido por teclado.
# 6. Mostrar todos los números.
# Realiza las opciones con funciones. Para crear un número aleatorio en python debes
# incluir la librería random (from random import uniform) y utilizar la función uniform(valorI,
# valorF) que devuelve un float comprendido entre el valorI y el valorF.
# from random import uniform
# arrayNumeros = []
# for i in range (100):
#     arrayNumeros.append(int(uniform(0, 10)))
# print (arrayNumeros)

def mayor(array):
    mayor = 0
    for i in array:
        if i > mayor:
            mayor = i
    return mayor

# print(mayor(arrayNumeros))

def menor(array):
    menor = len(array)
    for i in array:
        if i < menor:
            menor = i
    return menor

# print(menor(arrayNumeros))

def suma(array):
    suma = 0
    for i in array:
        suma += i
    return suma

#print(suma(arrayNumeros))

def media(array):
    resultado=suma(array)
    return resultado/len(array)

#print(media(arrayNumeros))

def sustituir(array,num):
    arrayNuevo = []
    for i in array:
        if i == num:
            i = 100
            arrayNuevo.append(i)
        else :
            arrayNuevo.append(i)
    return arrayNuevo

# print(sustituir(arrayNumeros, 6))

def mostrarNumeros(array):
    return array
    
# print(mostrarNumeros(arrayNumeros))


# print("1. Conocer el mayor de los números.\n" + "2. Conocer el menor de los números.\n" + 
# "3. Obtener la suma de todos los números.\n" + "4. Obtener la media de ellos números.\n" + 
# "5. Sustituir el valor de un elemento por otro número introducido por teclado.\n" +
# "6. Mostrar todos los números.\n" + "7.Salir")
# operacion = int(input("¿Que deseas realizar?"))
# while operacion != 7 :
#     if operacion == 1:
#         print(mayor(arrayNumeros))
#     elif operacion == 2:
#         print(menor(arrayNumeros))
#     elif operacion == 3:
#         print(suma(arrayNumeros))
#     elif operacion == 4:
#         print(media(arrayNumeros))
#     elif operacion == 5:
#         num = int(input("Dime el numero que quieres cambiar"))
#         print(sustituir(arrayNumeros, num))
#     elif operacion == 6:
#         print(mostrarNumeros(arrayNumeros))
#     operacion = int(input("¿Que otra operacion desea realizar"))





