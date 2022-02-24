'''Un juguete tiene tres botones, dos de melodías: A y B (con dos músicas por botón) y otro P de
apagado. Cada botón de melodía activa el juguete y al ser pulsado sucesivamente cambia de una a
otra melodía.
Es decir, si se pulsa el botón A una vez suena la melodía A1 y si se vuelve a pulsar, la A2, y de igual
modo sucede con el botón B.
Crea un programa que lea por teclado el botón que se ha pulsado (independientemente de si es
mayúscula o minúscula) y escriba la melodía que suena (melodía A1, … melodía B2) y se apague
cuando se pulse el botón P.'''
print("Hola")
tipo=input("Introduzca el botón deseado (A o B o P=Apagar)")
while tipo!="A" and tipo!="a" and tipo!="B" and tipo!="b" and tipo!="P" and tipo!="p":
    tipo=input("Error.Introduzca el botón deseado (A o B o P=Apagar)")
acumulador=1
acumulador1=1

    

while tipo=="A" or tipo=="a":
    if acumulador%2!=0:
        print("La melodía que suena es A1")
    if acumulador%2==0:
        print("La canción que suena es A2")
        
    acumulador+=1  
    tipo=input("Introduzca el botón deseado (A o B o P=Apagar)")

    
while tipo=="b" or tipo=="B":
    if acumulador1%2!=0:
        print("La melodía que suena es B1")
    if acumulador1%2==0:
        print("La canción que suena es B2")
    acumulador1+=1
    tipo=input("Introduzca el botón deseado (A o B o P=Apagar)")
if tipo=="p" or tipo=="P":
    print("El PROGRAMA HA TERMINADO")
        