print("Hola")
numero_entero=int(input("Introduce un numero entero: "))
numeropositivo=int(input("Introduce un numero entero positivo: "))
def mypower(numero_entero,numeropositivo):
    resultado=numero_entero
    if numeropositivo<0:
        resultado=-1
    if numeropositivo==0:
        resultado=1
    for i in range (1,numeropositivo):
        resultado=resultado*numero_entero
    return(resultado)
print ([mypower(numero_entero,numeropositivo)])
            