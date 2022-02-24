'''El índice de masa corporal o IMC es una medida que se utiliza para evaluar el riesgo de enfermedad
cardiovascular. Para su cálculo se divide el peso en kilogramos por la altura en metros elevados al
cuadrado, de forma que un peso normal o normopeso estaría situado en un valor de IMC entre 18,5 y
24,9.
Crea un programa que pida la altura, peso y edad de una persona y calcule e informe del valor y tipo
de IMC obtenido atendiendo al siguiente criterio:
<18,5 Peso insuficiente
18,5-24,9 Normopeso
25-29,9 Sobrepeso
30-39,9 Obesidad
>40 Obesidad mórbida
Además de facilitar el IMD, debe proporcionar un mensaje de recomendación sanitaria si la edad de
la persona es superior a 45 y excede el normopeso (IMC >25), o bien, si ésta tiene obesidad (IMC
>30). Por ejemplo:
Para un peso de 90 kilogramos y una talla de 1.80 metros, su IMC es: 27.78
Usted se encuentra en el grupo: Sobrepeso.
Caso 1 - Dada su edad e IMC es recomendable que cuide su salud cardiovascular
Caso 2 - Dado su IMC es muy recomendable que cuide su salud cardiovascular
Este programa debe validar la información proporcionada y terminar cuando se introduzca un valor
negativo en cualquier medida (edad, peso o tamaño).'''
print("Hola")
edad=int(input("Introduce una edad (Negativo para teminar) : "))
if edad<0:
    print("El programa ha terminado") #Al ser valor negativo mostramos mensaje de salida
else:
    altura=int(input("Introduce su altura en centimetros (Negativo para teminar):")) #En centimteros para su posterior paso a metros
    if altura<0:
        print("El programa ha terminado")
    else:
        peso=int(input("Introduce el peso en kilogramos (Negativo para teminar): "))
        if peso<0:
            print("El programa ha terminado")


if edad>=0 and altura>=0 and peso>=0:
    imc=peso/((altura/100)**2)#Pasamos la altura a metros y calculamos el IMC
    if imc<18.5:
        print("Peso insuficiente")
    elif imc>=18.5 and imc<=24.9:
        print("Normopeso")
    elif imc>=25 and imc<=29.9:
        print("Sobrepeso")
        if edad>45:
            print("Dada su edad, e IMC es recomendable que cuide su salud cardiovascular")
    elif imc>=30 and imc<=39.9:
        print("Obesidad")
        print("Es muy recomendable que cuide su salud cardiovascular")
    elif imc>40:
        print("Obesidad mórbida")
        print("Debería acudir a un profesional su imc es demasiado alto")
