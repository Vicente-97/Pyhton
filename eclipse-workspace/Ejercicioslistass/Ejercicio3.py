# 3. Realizar un programa que solicite la fecha como tres datos numéricos (día, mes y año).
# Deberá mostrar la fecha en formato largo.
# Introduce el día de la fecha: 15
# Introduce el mes de a fecha: 3
# Introduce el año de a fecha: 2009
# La fecha en formato largo es 15 de Marzo de 2009
# Si la fecha introducida es incorrecta se mostrará un mensaje de error: “Fecha incorrecta” y el
# programa terminará. El programa terminará cuando se introduzca un día negativo.
def adivinarMes(num):
    meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
    mes = ""
    for i in meses:
        if i == meses[num]:
            mes = meses[num - 1]
    return mes

print(adivinarMes(5))


dia = int(input("Dime un numero para el dia del mes"))
while dia >= 1 and dia <= 31:
    mes = int(input("Dime un numero para el mes del año "))
    anno = int(input("Dime un año"))
    print(str(dia) + " de " + adivinarMes(mes) + " de " + str(anno))
    dia = int(input("Dime un numero para el dia del mes pulsa un numero negativo para terminar:"))