from Ejercicio2listas import bisiesto
print("hola")
ano=int(input("Introduce el año: "))
mes=int(input("Introduce el numero de mes: "))
def daysmonth(mes,ano):
    meses=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    if bisiesto(ano)==1:
        meses[2]=29
    print("El año", ano ,"el mes ", mes,"tiene", (meses[mes]), " dias.")
daysmonth(mes,ano)
       
           

          
