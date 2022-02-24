# 14. Escribe una función que, dada una lista de cadenas, devuelva la cadena más larga. 
# Si dos o más cadenas miden lo mismo y son las más largas, la función devolverá 
# una cualquiera de ellas.
def cadenaMaslarga(listaCadena):
    cadenaLarga = ''
    for i in listaCadena:
        if len(i) > len(cadenaLarga):
            cadenaLarga = i
    return cadenaLarga

print(cadenaMaslarga(["ana","anilina","ruina"]))