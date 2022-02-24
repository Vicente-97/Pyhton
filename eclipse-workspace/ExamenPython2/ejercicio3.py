def divisores(num):
    contadordivisores=[]
    
    for i in range (1,num+1):
        if num%i==0:
            contadordivisores.append(i)
            
    return contadordivisores

print(divisores(15))


def esprimo(num):
    resultado=False
    contador=0
    for i in range (1,num+1):
        if num%i==0:
            contador+=1
        if contador==2:
            resultado=True
    return resultado

print(esprimo(7))


def Coprimos(num1,num2):
    if divisores(num1)[1]==divisores(num2)[1]:
        resultado=False
    elif divisores(num1)[0]==divisores(num2)[0]:
        resultado=True 
        
        
    return resultado

print(Coprimos(14,15))
print(Coprimos(14,8))






        