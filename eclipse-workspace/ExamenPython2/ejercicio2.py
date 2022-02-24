

def encontrarpalabra (palabra,):
   
    numeroApariciones=0
    cadenaADN=["AATCGACTTGCCAGCGACTACTACTAA"]
    posicion=0
    palabrascoincidencia=[]
    
    for i in (len(palabra)):
        for j in (len(cadenaADN)):
            if palabra[i] in cadenaADN:
                palabrascoincidencia+=[i+3]
            
        
            
           
            
           
            
        
        
    return palabrascoincidencia


print(encontrarpalabra("CGACT"))




        


