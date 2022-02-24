'''9. Escribir una función que reciba una lista de números enteros y
 un entero k, escribir tres funciones, una que devuelva una lista con los
  menores de k, otra función devuelva los mayores y otra los iguales a k. 
  Por último otra función que devuelva una lista con aquellos que son múltiplos de k.'''
def listaYEntero():
    lista=[]    
    for i in range(10):
        numero=int(input("Introduce un numero"))
        lista.append(numero)
    return lista
#print(listaYEntero())

def mayorQueNumero(lista,k):
    listaMayor=[]
    for i in lista:
        if i>k:
            listaMayor.append(i)
    return listaMayor
#print(mayorQueNumero(listaYEntero(), 26))

def menorQueNumero(lista,k):
    listaMenor=[]
    for i in lista:
        if i<k:
            listaMenor.append(i)
    return listaMenor
#print(menorQueNumero(listaYEntero(), 26))

def multiploNumero(lista,k):
    listaMultiplo=[]
    for i in lista:
        if k%i==0:
            listaMultiplo.append(i)
    return listaMultiplo
#print(menorQueNumero(listaYEntero(), 10))
