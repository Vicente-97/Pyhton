
#lista=[]
#resultado=False
def ecuentrapalabra(cadena,palabra):
    resultado=False
    sitio=0
    palabragood=""
    cadena+=" "
    for i in cadena:
        if palabragood==palabra:
            resultado=True
        elif palabra[sitio]==i:
            palabragood+=i
            sitio+=1
            
            
        
    return resultado

print(ecuentrapalabra("shybaoxlna", "hola"))

