



def CambioPosicion (palabra, numPosicion):
    abecedario="abcdefghijklmnñopqrstuvwxyz"
    palabranueva=""
    
    
    for i in palabra:
        
        for j in range (len(abecedario)):
            if i in abecedario[j]:
                palabranueva+=abecedario[j+numPosicion]
            
                
                
            
            
    return palabranueva


print(CambioPosicion("casado", 3))
            
            
    