def VocalYConsonante (cadena):
    vocal = "aeiou"
    salida=""
    vocales=""
    conso="bcdfghjklmnñpqrstvwxyz"
    consonantes = ""

    for i in range (len(cadena)):
            if cadena[i] in vocal:
                vocales+=cadena[i]
                
                
            elif cadena[i] in conso:
                consonantes+=cadena[i]
    
    salida=consonantes+vocales
        
    return salida
        
print (VocalYConsonante("curso de programacion"))
        
        
        
        
        
    
    
    
    
    
    
    
    
    
