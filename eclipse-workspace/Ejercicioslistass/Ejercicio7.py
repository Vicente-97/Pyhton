# 7. Escribir una función que indique si dos fichas de dominó encajan o no. Cada ficha es
# recibida como una lista de dos valores, por ejemplo:[3,4] ,[2,5].
# ficha1=[3,4]
# ficha2=[4,5]
#
# def domino(ficha1,ficha2):
#     if ficha1[0] == ficha2[0] or ficha1[0] == ficha2[1] or ficha1[1] == ficha2[0] or ficha1[1] == ficha2[1]:
#         return True
#     else : 
#         return False
#
# print(domino(ficha1, ficha2))


array=[[3,4],[4,5]]


# for ele in array:
#     print(ele)
#     for i in ele:
#         print(i)

def dominoUnaLista(array):
    if len(array) != 2: 
        print("Error, tiene que ser menos fichas")
    else:
        ficha1 = array[0]
        ficha2 = array[1]
        encontrado = False
        for i in ficha1:
            for i in ficha2 :
                encontrado = True 
        return encontrado
    
print(dominoUnaLista(array))
    