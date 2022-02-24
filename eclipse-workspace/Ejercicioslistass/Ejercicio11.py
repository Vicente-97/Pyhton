# 11. Escribe una función que reciba dos listas 
# y devuelva una lista con los elementos comunes a
# ambas, sin repetir ninguno.

def elementosComunes(lista1,lista2):
    listaComun = []
    for i in lista1:
        for j in lista2:
            if i == j and i not in listaComun:
                listaComun.append(i)              
    return listaComun
    
print(elementosComunes([1,8,6,7,9,2,6], [9,8,11,12,6,9]))