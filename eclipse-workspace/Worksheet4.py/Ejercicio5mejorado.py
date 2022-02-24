'''def palyndrome(cadena):
resultado=True
for i in range(len(cadena)//2):
if cadena[i]!=cadena[-i-1]:
resultado = False
return resultado
print(palyndrome("anilina"))'''
"""
def palyndrome(cadena):
resultado=True
contador=0
while resultado and contador<=len(cadena)//2:
contador+=1
if cadena[contador]!=cadena[-contador-1]:
resultado = False
return resultado
print(palyndrome("anilina"))"""

def palyndrome(cadena):
    resultado=False 
    lista=[]
    listaAlreves=[]
    
    for i in range (len(cadena)):
        lista.append(cadena[i])
        for j in range (len(cadena)):
            listaAlreves.append(cadena[i-1])
            if lista==listaAlreves:
                resultado=True 
                
    return resultado

print(palyndrome(""))






        