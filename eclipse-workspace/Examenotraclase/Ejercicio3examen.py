'''3.- Vamos a escribir un programa para codificar una clave que el usuario deberá introducir por
teclado, así, cuando sepamos escribir en ficheros, en vez de guardar la clave guardaremos la
codificación, aunque por ahora lo que haremos es escribirla por pantalla.
La generación de la clave se hará en función de la seguridad que quiera el usuario por lo que lo
primero que debemos hacer es pedirle cuántos números quiere introducir para generar la clave. A
continuación se le deberán preguntar los números y la clave se generará sumando el resto de dividir
los números entre 5, siempre y cuando los números sean impares. Aunque se introduzcan números
negativos se debe sumar el resto nunca restar.
Es decir, el programa debe preguntar ¿cuántos números quieres para la clave? Si le digo por
ejemplo 6, debe preguntarme los seis números, si mi respuesta es:
235 → El resto es 0, no tengo que hacer nada
458 → El resto es 3 es impar lo sumo
6 → El resto es 1, es impar lo sum
-679 → El resto es -4, es par, no lo sumo
89 → El resto es 4, es par, no lo sumo
-88 → El resto es 3, es impar, lo sumo
El resultado de la clave es 7'''
print("Hola rellene el siguiente cuestionario: ")
cantidadnumeros=int(input("Introduzca la cantidad de numeros para generar la clave: "))
clave=0
for i in range (cantidadnumeros):
    numeros=int(input("Introduzca numero: "))
    resto=numeros%5
    if resto%2!=0:
        clave=clave+resto
    
        
    
print (clave)

        
    
