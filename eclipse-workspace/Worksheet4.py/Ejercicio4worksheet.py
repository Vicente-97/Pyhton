def numberinString(cadena):
    cont=0
    for i in range (len(cadena)):
        if (cadena[i].isdigit()):
            cont+=1
    return cont
print (numberinString("JavierAA5643AAaa"))
