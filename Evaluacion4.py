usuarios = []

def RegistraUsuario():
    nombre = input("Ingrese su nombre: ").lower()

def validar_sexo(sexo):
    if sexo.upper() not in ['M', 'F']:
        return "El sexo debe ser 'M' o 'F'."
    return None

def validarCantidadCaracter(contraseña):
    
    if len(contraseña)>=8:
        return True
    else:
        return False

def ValidarContraseña(contraseña):
   
    if validarCantidadCaracter(contraseña)== 0:
        print("*El código debe tener al menos un número*")
        return False
    elif validarCantidadCaracter (contraseña)==False:
        print ("*El codigo debe tene un largo de al menos 8 caracteres")
        return False
    else:
        return True
    
def BuscarUsuario(nombre):
    for nombre in usuarios:
        if nombre ():
            return nombre
    return None
        #print("-"*60)
        #print(f"Nombre: {nombre} \t Sexo: {sexo} \t contraseña: {contraseña}")
        #print("-"*60)
        #return [nombre,sexo,contraseña]

def EliminarUsuario(nombre):
    nombre = ("Ingrese el nombre de usuario que desea eliminar: ")
    nombreEncont= nombre(usuarios)
    if nombreEncont!=None:
        usuarios.remove(nombreEncont)
        return True
    else:
        return False
    

def menu():
    while True:
        print ("---MENÚ---")
        print("1.- Ingresar Usuario")
        print("2.- Buscar Usuario")
        print("3.- Eliminar Usuario")
        print("4.- Salir")
    
        opcion = input("Seleccione una opcion: ").strip
    if opcion == "1":
        RegistraUsuario()
    
    elif opcion == "2":
        BuscarUsuario()
    
    elif opcion == "3":
        EliminarUsuario()
    
    elif opcion == "4":
        print ("Programa terminado")
    
        pass
    else:
        print ("Debe ingresar una opción válida")

menu()