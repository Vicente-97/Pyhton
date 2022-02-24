# 5. Realizar un función que reciba una lista y devuelva una nueva lista cuyo contenido sea igual
# a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’], deberá
# devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’]. Llamar a dicha función
array=["Di", "buen", "dia", "a", "papa"]

def invertirArray(array):
    arrayInvertido=[]
    contPalabras=0
    while contPalabras != len(array):
        contPalabras += 1
        ultimaPosicion = array[len(array)-contPalabras]
        arrayInvertido.append(ultimaPosicion)
    return arrayInvertido

# print(invertirArray(array))