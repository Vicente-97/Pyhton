#2. Realiza un programa que lea 10 números, debe imprimir los 10 número y después
# desplazarlos una posición, de tal forma que el último pase a la primera posición, el primero a
# la segunda, el segundo a la tercera, y así sucesivamente
array=[]
for i in range(10):
    num=int(input("Dime un numero"))
    array.append(num)
print(array)

def cambiarPosicion(array):
    arrayCambiado = []
    posicion = array[len(array)-1]
    arrayCambiado.append(posicion)
    for i in range (len(array)-1):
        arrayCambiado.append(array[i])
    return arrayCambiado
        
print(cambiarPosicion(array))


def cambiarPosicionAlternativa(array):
    ultimoNum = array[len(array)-1]
    posicion = len(array)-1
    while posicion >= 0:
        array[posicion] = array[posicion-1]
        posicion-=1
    array[0]=ultimoNum
    return array

print(cambiarPosicionAlternativa(array))