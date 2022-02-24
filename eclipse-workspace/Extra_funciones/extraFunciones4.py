
lista=[]
    
lista.append(['alejandra','pass1',0])
lista.append(['daniel','pass2',0])


def login_Usuario (usuario, contrasena):
    existeUsuario=False

 
    for i in lista:
        if i[0]==usuario:
            print("Usuario Encontrado")
            if i[2]==3:
                print("Usuario Bloqueado")
            elif i[1]==contrasena:
                print("Contraseña Correcta")  
                existeUsuario=True   
            else:
                i[2]+=1
            
    return existeUsuario

def interfaz():
    usuario=" "
    while usuario!="":
        usuario=input("Introduzca usuario:")
        contrasena= input("Introduzca la password")
        if login_Usuario(usuario,contrasena)==True:
            print("usuario valido")
        else:
            
            print("Usuario erroneo")
            
        print(lista)

             


interfaz()
login_Usuario(usuario, contrasena)


  
            
