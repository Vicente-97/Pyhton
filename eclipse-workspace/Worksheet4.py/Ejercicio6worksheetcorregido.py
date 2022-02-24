
def existeEscondida(cadena,palabraEscondida):
    estaEscondida=True
    if len(cadena) < len(palabraEscondida):
        estaEscondida=False
    elif len(cadena) == len(palabraEscondida):
        estaEscondida = (cadena==palabraEscondida)
        
    else: #Palabra es menor que la cadena
        posicionPalabra=0
        for i in cadena:
            if palabraEscondida[posicionPalabra]==i:
                posicionPalabra+=1
        if estaEscondida!=palabraEscondida:
            estaEscondida=False
    return estaEscondida

print (existeEscondida("shybaoxlna", "hola"))
            
            