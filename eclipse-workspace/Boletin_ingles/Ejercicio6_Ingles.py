print("Hola rellene lo siguiente: ")
num1=int(input("Introduce el primer numero: "))
num2=int(input("Introduce el segundo numero: "))
resultado=num1
for i in range (1,abs(num2)):
    resultado=resultado+num1
if num2<0:
    resultado=-resultado
print(resultado)

