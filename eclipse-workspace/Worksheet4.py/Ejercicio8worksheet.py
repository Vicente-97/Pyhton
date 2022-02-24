def cuentaVocalesdiferentes(palabra):
    palabram=str.lower(palabra)
    vocales = "aeiou"
    resultado=0
    lista=[0,0,0,0,0]
    for letra in palabram:
        for i in range (len(vocales)):
            if letra == vocales[i]:
                lista[i]+=1
    if lista[0]>0:  
        resultado+=1
    if lista[1]>0:
        resultado+=1
    if lista[2]>0:
        resultado+=1
    if lista[3]>0:
        resultado+=1
    if lista[4]>0:
        resultado+=1
            
        
            
    return resultado
print(cuentaVocalesdiferentes("palabra"))
    