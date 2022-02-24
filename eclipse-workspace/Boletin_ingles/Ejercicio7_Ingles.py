print("Hola rellene lo siguiente: ")
veces=(int(input("Introduce cuantos numeros desea ingresar: ")))
resultado=0
for i in range (veces):
    numero=(int(input("Introduce un numero mayor que 0: ")))
    if numero>0:
        resultado+=numero
    else:
        print("El numero no es valido, debe de ser mayor que 0.")
        numero=(int(input("Introduce un numero mayor que 0: ")))

print("la media es", resultado/veces)