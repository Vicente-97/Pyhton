'''8. Realizar un programa que pida números enteros hasta que se introduzca un 
número negativo. Escribir una función que:
1. Devuelva una lista con todos los que sean primos.
2. Devuelva la suma y el promedio de todos los valores.
3. Devuelva una lista con el factorial de cada uno de esos números.'''
listaNumeros=[]
numero=(int(input("Introduce un numero")))
while numero>=0:
    listaNumeros.append(numero)
    numero=(int(input("Introduce un numero")))

def primo(listaNumeros):
    listaPrimos=[]
    for i in listaNumeros:
        esPrimo=True
        for j in range(2,i):
            if i%j==0:
                esPrimo=False
        if esPrimo==True:
            listaPrimos.append(i)
    return listaPrimos
print(primo(listaNumeros))

def sumaYPromedio(listaNumeros):
    resultado=sum(listaNumeros)
    return resultado, resultado/len(listaNumeros)
print(sumaYPromedio(listaNumeros))

def factorial(num):
        resultado=1
        for i in range(1,num+1):
            resultado*=i
        return resultado

def factorialNumero(listaNumeros):
    listafctorial=[]
    for i in listaNumeros:
        listafctorial.append(factorial(i))
    return listafctorial
print(factorialNumero(listaNumeros))
