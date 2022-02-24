def complementaria (cadena):
    cadenaNueva=""
    for i in cadena:
        if i=="A":
            i="T"
            cadenaNueva+=i
        elif i=="T":
            i="A"
            cadenaNueva+=i  
        elif i=="G":
            i="C"
            cadenaNueva+=i  
        elif i=="C":
            i="G"
            cadenaNueva+=i
        
    return cadenaNueva

print(complementaria("TGACTGGTCAA")) 

"ACTGACCAGTT"  