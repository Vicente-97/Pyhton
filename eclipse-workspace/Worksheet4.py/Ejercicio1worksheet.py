
def charactersInString(cadena,caracter):
    numcaracter=0
    for i in range (len(cadena)):
        if str.lower(caracter)==str.lower(cadena[i]):
            numcaracter+=1
    return numcaracter
print(charactersInString("JaAaaaavier","a"))



