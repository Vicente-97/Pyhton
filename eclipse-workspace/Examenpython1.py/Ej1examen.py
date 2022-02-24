'''Juan recibe un regalo económico de su familia todos sus cumpleaños, de forma que cada año recibe
15€ más que en el anterior.
Elabora un programa que pida una edad y calcule cuánto dinero en total ha recibido Juan en regalos
de cumpleaños hasta esa edad sabiendo que en el primer cumpleaños le regalaron 20€.
Ejemplo 1: 1 año ⇒ 20€ (recibe el 1º año)
Ejemplo 2: 2 años ⇒ 55€ (= 20€ tenía +35€ recibe el 2º año)
Ejemplo 3: 3 años ⇒ 105€ (= 55€ tenía +50€ recibe el 3º año)
Ampliación: modifica el programa anterior para que tanto la cantidad que se incrementa cada año
como el regalo inicial cambien en cada programa.'''
print("Hola")
edad=int(input("Introduce una edad: ")) #Introducimos la edad
while edad<0:
    edad=int(input("Error.Introduce una edad: ")) #En caso de fallo vuelve a pedir la edad
resultado=20
acumulador=15
for i in range (1,edad):
    resultado=resultado+acumulador
    acumulador+=+15
print("Juan recibió a la edad de ", edad, "años", resultado,"euros.")