# 12. Escribe una función que reciba dos listas y devuelva los elementos que 
# pertenecen a una o a otra, pero sin repetir ninguno (unión de conjuntos).
def elementosNoComunes(lista1,lista2):
    listaNoComun = []
    for i in lista1:
        for j in lista2:
            if i != j and i not in listaNoComun:
                listaNoComun.append(i)
            elif j not in listaNoComun:
                listaNoComun.append(j)            
    return listaNoComun
    
print(elementosNoComunes([1,8,6,7,9,2,6], [9,8,11,12,6,9]))