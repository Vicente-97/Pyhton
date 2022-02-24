# 13. Escribe una función que, dada una lista de nombres y una letra, 
# devuelva una lista con todos los nombres que empiezan por dicha letra.
def empiezaPorLetra(listaNombres,letra):
    listaNombresConLetra=[]
    for i in listaNombres:
        if i[0] == letra and i not in listaNombresConLetra:
            listaNombresConLetra.append(i)
    return listaNombresConLetra

print(empiezaPorLetra(["ana","anilina","ruina"], "a"))