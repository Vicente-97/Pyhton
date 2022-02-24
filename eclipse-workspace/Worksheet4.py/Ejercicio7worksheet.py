def buscaYRemplaza (cadena,palBuscar, palRemplazar):
    salida=""
    if len(cadena)>len(palBuscar):
        for i in range (len(cadena)):
            cont=0
            if cadena[i]==palBuscar[0]:
                coincide = True 
                for j in range (len(palBuscar)):
                    if (i+j) < len(cadena) and palBuscar[j]!=cadena[i+j]: 
                         coincide = False 
                if coincide:
                    salida+=palRemplazar
            else:
                salida+=cadena[i]

    return salida
cadena = "La lluvia en Sevilla es una Maravilla"
palBuscar = "lluvia"
palRemplazar= "calor" 
print(buscaYRemplaza(cadena, palBuscar, palRemplazar))