print("Hola rellene lo siguiente: ")
numero=(int(input("Introduce un numero mayor que 0: ")))
while numero<=0:
    numero=(int(input("Error.Introduce un numero mayor que 0: ")))
pregunta=input("Desea introducir mas numeros (Y=Yes or N=No): ")
while pregunta!="Y" and pregunta!="N":
    pregunta=input("Desea introducir mas numeros (Y=Yes or N=No): ")
numeropeque=numero
while (pregunta)=="Y":
    numero=(int(input("Introduce un numero mayor que 0: ")))
    while numero<=0:
        numero=(int(input("Error.Introduce un numero mayor que 0: ")))
    if numero<numeropeque:
        numeropeque=numero
    pregunta=str(input("Desea introducir mas numeros (Y=Yes or N=No): "))
    while pregunta!="Y" and pregunta!="N":
        pregunta=input("Desea introducir mas numeros (Y=Yes or N=No): ")

print("El numero mas pequeño es ", numeropeque)