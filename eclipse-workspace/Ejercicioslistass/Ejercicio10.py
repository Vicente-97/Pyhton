# 10. Escribe una función para pasar un número de binario a 
# decimal y de decimal a binario
from Ejercicio5 import invertirArray

def pasarBinarioADecimal(numBinario):
    posicionExponente = 0
    resultado = 0
    for i in range (len(numBinario)-1,-1,-1):
        resultado = resultado + numBinario[i] * (2 ** posicionExponente)
        posicionExponente += 1
    return resultado

# print(pasarBinarioADecimal([1,1,1,0]))


def pasarDecimalABinario(numDecimal):
    resultado = []
    while numDecimal >= 1 :
        resto = numDecimal % 2
        numDecimal = numDecimal // 2
        resultado.append(resto)
    return resultado

print(invertirArray(pasarDecimalABinario(11)))