#print("Hola")
#ano=int(input("Introduzca un año: "))
#while ano<=0:
    #ano=int(input("Error.Introduzca un año: "))
def bisiesto(ano):
        anobisiesto=0
        if ano%400==0:
            anobisiesto=1
        elif ano%4==0 and ano%100!=0 and ano%400!=0:
            anobisiesto=1
        else:
            anobisiesto=-1
        return anobisiesto
#print(bisiesto(ano))