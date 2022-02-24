
def lowInCaseString(cadena,caracter):
    num=0
    for i in range (len(cadena)):
        if str.lower(caracter)==(cadena[i]):
            num+=1
    return num
print (lowInCaseString("JavierAaaa","a"))