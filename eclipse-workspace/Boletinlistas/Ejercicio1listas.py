print("Hola")
numero=int(input("Introduce un numero: "))

def factorial(numero):
    suma=numero
    if numero>=0:
        for i in range (1,numero):
            suma=suma*i
    else:
        suma=-1   
    return suma
print("El factorial de ", numero, "es",factorial(numero))
        


