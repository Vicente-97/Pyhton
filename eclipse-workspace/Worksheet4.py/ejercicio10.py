def numeroPalabras (cadena):
    
    contadorPalabras=0
    
    for i in range (len(cadena)):
        if cadena[i]==" ":
            contadorPalabras+=1
        if cadena[i]==".":
            contadorPalabras+=1
        if cadena[i]==" "+" ":
            contadorPalabras+=1
        if cadena[i]==",":
            contadorPalabras+=1
        
    return contadorPalabras

print(numeroPalabras("he estudiado mucho."))
    
    
            