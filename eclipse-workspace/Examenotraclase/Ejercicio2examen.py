'''2.- Seguimos trabajando para un centro de salud y nos piden que digamos cuántos enfermos de los
que han pasado el covid son menores de 30 años, cuántos tienen entre 31 y 49 años (49 incluidos) y
cuántos hay de los que tengan 50 o más años. Para ello van a llamar a todos los pacientes que han
pasado el covid y le van a preguntar la edad, debemos diseñar un programa que vaya pidiendo el
mes y el año de nacimiento de los enfermos, calcule la edad que tienen (piensa que si cumple en
noviembre lo vamos a contar como que ya ha cumplido aunque por ejemplo cumpla a finales de
mes y lo llamen el día 2) y lo contabilice en el tramo correspondiente. El programa terminará
cuando el usuario introduzca un -1 en el mes de nacimiento.
Ten en cuenta que si el usuario introduce un mes en negativo no debe pedirle el año, ya que debe
mostrar los resúmenes y salir.
• Posible mejora a implementar si sabes, ¿cómo podrías hacer para que fuese fácil cambiar el
mes y el año en el que se ejecuta tu programa? Escribe la respuesta en el mismo fichero de
Python'''
print("Hola rellene el siguiente cuestionario: ")
numeropacientes=int(input("Cuantos pacientes han pasado el covid: "))
mesactual=int(input("Introduce el mes actual: "))
resultado=0
resultadomes=0
contador1=0
contador2=0
contador3=0
for i in range (numeropacientes):
    ano=int(input("Introduzca el año del paciente (-1 para terminar): "))
    mes=int(input("Introduzca el numero de mes del paciente: "))
    resultado=2020-ano
    resultadomes=mesactual-mes
    if mesactual>=mes:
        resultado+=1
    if resultado<=30:
        contador1+=1
    if resultado>=31 and resultado<=41:
        contador2+=1
    if resultado>=50:
        contador3+=1
print("Hay ", contador1, "pacientes menores de 30 años", ",",contador2, " pacientes entre 31 y 41 años", contador3, ",", " pacientes mayores de 50 años.")
    
    