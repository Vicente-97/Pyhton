def OrdenarNumero (numeroMayor, numeroMenor):
    if numeroMayor<numeroMenor:
        return numeroMenor, numeroMayor
    else:
        return numeroMayor, numeroMenor
    
    
    
    
    
def CalcularMCD (numeroMayor, numeroMenor): 
    numeroMayor, numeroMenor= OrdenarNumero(numeroMayor, numeroMenor)
    
    resto= numeroMayor%numeroMenor
    if resto==0:
        return numeroMenor
    
    else:
        numeroMenor%resto
        
        
numeroMayor=int(input("Introduce un numero Mayor"))
numeroMenor=int(input("Introduce un numero menor"))

print(CalcularMCD(numeroMayor, numeroMenor))
        
        
        
        