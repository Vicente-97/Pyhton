print("Hola rellene lo siguiente: ")
veces=int(input("Cuantos numeros desea ingresar: "))
for (i) in range (veces):
    numero=int(input("Ingrese un numero mayor que 0: "))
    if numero<0:
        print("El numero no es valido, debe ser mayor que 0 ")
    elif numero%2==0:
        print("El numero es par")
    elif numero%2==1:
        print("El numero es impar")
    
    