# 6. Realizar una función que reciba una lista y devuelva si está ordenada o no. Llamar a dicha
#función.
arrayCadena = ["a","b","c","d"]

def Ordenado(array):
    bandera = True
    for i in range (len(array)-1):
        if array[i] > array[i + 1]:
            bandera = False
    return bandera
        
print(Ordenado(arrayCadena))