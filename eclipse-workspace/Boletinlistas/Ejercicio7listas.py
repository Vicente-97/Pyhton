print("Hola")
numero=int(input("Introduce un numero positivo: "))

def isprime(numero):
    contador=0
    contador2=0
    for i in range(1,(numero+1)):
        contador2+=1
        if numero%i==0:
            contador+=1
        
    if contador==2:
        print("El numero es primo")
    else:
        print("El numero no es primo")
    print(contador2)   
    
    return
isprime(numero)

       