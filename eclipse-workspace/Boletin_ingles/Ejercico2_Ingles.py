print("Hola rellene el siguiente cuestionario: ")
numero=int(input("Ingrese un numero del 1 al 10: "))
if numero<0 or numero>10:
    print("Error")
else:
    for i in range (0,11):
        resultado=i*numero
        print(numero, "x", i, "= " , resultado)

    
