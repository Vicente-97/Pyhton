
print("Hola")
entero=int(input("Introduce un numero: "))
def numbersofnumbers(entero):
    if entero<0:
        entero=-1
        print("El resultado es ", entero)
    elif entero>=0:
        entero=str(entero)
        print ("El numero tiene ", len(entero), " cifras.")
numbersofnumbers(entero)
    
    