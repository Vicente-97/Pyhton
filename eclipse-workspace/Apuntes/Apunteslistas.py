'''
Tipos basicos
Tipos compuesto:
Lista-->
insert, remove, append, len'''

lista=[1,3,3,5]
lista.append(15) #Insertar al final
lista.insert(1,80)
lista.remove(5) #Elimina el elemento indicado

tamanyo=len(lista) #Nos proporciona el tamaño de la coleccion
print(f'El tamaño de la lista es {tamanyo}')
print(f'La lista tiene estos elementos {lista}')

for elemento in lista:
    print(elemento)

lista2=[]
for i in range(1,16):
    lista2.append(i)

print(f'La lista tiene estos elementos {lista2}')

for i in range(len(lista)):
    print(lista[i])#Acceso indexado a los elementos de una lista.
nombre='Javier Villarreal Hinojo'
for i in range(len(nombre)):
    print(nombre[i])#Nombre letra por letra
cadena=""
print(len(cadena))
print(cadena[0])

if len(cadena) < len(palabra):
    resultado=True