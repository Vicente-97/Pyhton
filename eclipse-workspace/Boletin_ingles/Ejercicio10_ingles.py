print ("Hola rellene lo siguiente: ")
numero=int(input("Introduce un numero mayor que 0: "))
suma=1
while numero<0:
    numero=int(input("Error.Introduce un numero mayor que 0: "))
#Mientras que el numero sea menor que cero, te volverá a preguntar el numero
if numero>0:
    for i in range (1,numero+1):
            suma=suma*i
print("El numero factorial es ",suma)
