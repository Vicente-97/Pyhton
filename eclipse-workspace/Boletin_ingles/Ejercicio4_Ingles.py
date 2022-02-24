print("Hola rellene el siguiente cuestionario")
#Variable que almacenara la suma de los numeros.
acumulador=0
#Peticion de datos, si el numero es menor, no valido.
numero=int(input("Introduce un numero mayor que 0: "))
while numero<0:
    print("El numero no es correcto, intentalo de nuevo: ")
    numero=int(input("Introduce un numero mayor que 0: "))
#i va a tomar los valores desde el 1 hasta el numero.
for i in range (1, numero +1):
    acumulador = acumulador+i
#Impresion de resultados.
print("La suma de los numeros es" , acumulador)