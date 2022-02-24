def upperCaseString(cadena,caracter):
    num=0
    for i in range (len(cadena)):
        if str.upper(caracter)==(cadena[i]):
            num+=1
    return num
print (upperCaseString("JavierAAAAaa","a"))