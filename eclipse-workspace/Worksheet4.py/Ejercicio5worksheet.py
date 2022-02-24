def palindromo(palabra):
    palindro=[]
    palabrabien=[]
    for i in range (len(palabra)):
        palabrabien.append(palabra[i])
    for i in range (len(palabra)-1,-1,-1):
        palindro.append(palabra[i])
    if palabrabien==palindro:
        return ("Es un palindromo")
    else:
        return ("No es un palindromo")

print (palindromo("ana"))


def palyndrome(cadena):
    cadenainvertida=""
    for i in cadena:
        cadenainvertida=i+cadenainvertida
    return cadenainvertida==cadena

print(palyndrome("ana"))
        