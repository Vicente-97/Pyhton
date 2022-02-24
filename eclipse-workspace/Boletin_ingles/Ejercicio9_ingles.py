print ("Hola rellene lo siguiente: ")
numero=int(input("Introduce un numero mayor que 0: "))
suma=0
while numero<=0:
    numero=int(input("Error.Introduce un numero mayor que 0: "))
#Mientras que el numero sea menor que cero, te volverá a preguntar el numero
if numero>0:
    for i in range (1,numero):
        if numero%i==0:
            suma=suma+i
#Se comprobará numero por numero hast llegar al numero introducido si tiene resto cero.
#Si tiene el resto cero, que se sume el numero.
    if suma==numero:
        print("El numero es perfecto")  
    else:
        print("El numero no es perfecto")   
    