
def charactersinString(caracter,Palabra):
    contador=0
    for i in range(len(Palabra)):
        if (str.lower(Palabra[i]))==str.lower(caracter):
            contador+=1
    return contador
print(charactersinString("a", "JuliaAAAAaaan"))
        