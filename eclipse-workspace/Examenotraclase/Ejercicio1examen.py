'''1.- Realiza un programa que le pida al usuario su edad y que le pregunte si ha pasado el Covid o no,
así como si ha recibido la vacuna de Pfizer, Moderna o Astrazeneca. En función de la respuesta se
debe informar al usuario si debe volver a vacunarse o no teniendo en cuenta las siguientes
condiciones:
• Si ha recibido Astrazeneca, haya pasado el covid o no e independientemente de la edad debe
volver a vacunarse.
• Si ha recibido Moderna y es mayor de 60 años, sólo debe volver a vacunarse si no ha pasado
el covid. En otro caso, lo que han recibido Moderna no deben volver a vacunarse.
• Si ha recibido Pfizer y no ha pasado el covid, debe volver a vacunarse, y si lo ha pasado sólo
se vacunará si es mayor de 70 años.
Si el usuario no introduce los valores correctos, se debe mostrar un mensaje de error y volver a
solicitar los datos hasta que el usuario introduzca los datos de forma correcta.'''

print("Hola rellene el siguiente cuestionario: ")

edad=int(input("Introduzca su edad: "))
while edad<0:
    edad=int(input("Error.Introduzca su edad: "))
    
Covid=input("Ha pasado usted el Covid (S=Si , N=No): ") 
while Covid!="S" and Covid!="N":
    Covid=input("Error. Ha pasado usted el Covid (S=Si , N=No): ")
    
Vacuna=input("Vacuna recibida (Pfizer, Moderna o Astrazeneca): ")
while Vacuna!="Pfizer" and Vacuna!="Moderna" and Vacuna!="Astrazeneca":
    Vacuna=input("Error. Introduca la vacuna recibida (Pfizer, Moderna o Astrazeneca): ")
    
if Vacuna=="Astrazeneca":
    print("Debe volver a vacunarse")
elif edad>60 and Vacuna=="Moderna" and Covid=="N":
    print("Debe volver a vacunarse")
elif Vacuna=="Pfizer" and Covid=="N":
    print("Debe volver a vacunarse")
elif Vacuna=="Pfizer" and Covid=="S" and edad>70:
    print("Debe volver a vacunarse.")
else:
    print("No debe volver a vacunarse.")
