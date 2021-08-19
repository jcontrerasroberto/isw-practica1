import dbmanager as db
import os

def agregar_cliente():
    print("\n")
    print("AGREGAR CLIENTE")
    alias = input("Alias (max 10 caracteres): ")
    nombre = input("Nombre (max 30 caracteres): ")
    primer_apellido = input("Primer apellido (max 20 caracteres): ")
    segundo_apellido = input("Segundo apellido (max 20 caracteres - Opcional): ")
    razon_social = input("Razon social: ")
    rfc = input("RFC: ")
    telefono = input("Telefono (10 digitos): ")
    correo = input("Correo: ")
    cliente = (alias, nombre, primer_apellido, segundo_apellido, razon_social, rfc, telefono, correo)
    print("")
    if db.add_client(cliente):
        print("Cliente agregado correctamente")
    else:
        print("El cliente ya existe")
    
def actualizar_cliente():
    print("\n")
    print("ACTUALIZAR CLIENTE [DEJAR VACIO CAMPOS QUE NO QUIERES ACTUALIZAR]")
    alias = input("Alias del cliente a actualizar (max 10 caracteres - NO MODIFICABLE): ")
    nombre = input("Nuevo Nombre (max 30 caracteres): ")
    primer_apellido = input("Nuevo Primer apellido (max 20 caracteres): ")
    segundo_apellido = input("Nuevo Segundo apellido (max 20 caracteres - Opcional): ")
    razon_social = input("Nueva Razon social: ")
    rfc = input("Nuevo RFC: ")
    telefono = input("Nuevo Telefono (10 digitos): ")
    correo = input("Nuevo Correo: ")
    cliente = (nombre, primer_apellido, segundo_apellido, razon_social, rfc, telefono, correo, alias)
    print("")
    if db.update_client(alias, cliente):
        print("Cliente actualizado correctamente")
    else: print("El cliente no existe")

def listar_clientes():
    print("\n")
    print("LISTADO DE CLIENTES")
    rows = db.get_all()
    for row in rows:
        print("    " + row[1] + " " + row[2] + " "+row[3] +  " -> ( " + row[0]  + " )")

def eliminar_cliente():
    print("\n")
    print("ELIMINAR CLIENTE")
    alias = input("Ingresa el alias del cliente a eliminar: ")
    if db.delete_client(alias): print("Usuario " + alias + " eliminado")

def login():
    if db.isKey():
        key = input("Ingresa la clave: ")
        return db.checkKey(key)
    else:
        key = input("Nueva clave para ingresar al programa (max 50 caracteres): ")
        if key:
            return db.setKey(key)
        else: return False        

def menu_print():
    print("\n")
    print("Menu de administracion de usuarios")
    print("1. Agregar Cliente")
    print("2. Modificar Cliente")
    print("3. Eliminar Cliente")
    print("4. Listar Clientes")
    print("5. Salir")

def menu():
    menu_print()
    opc = input("Coloca la operacion que deseas realizar:")
    while opc not in ["1", "2", "3", "4", "5"]:
        opc = input("Coloca la operacion que deseas realizar:")
    if(opc == "1"): agregar_cliente()
    if(opc == "2"): actualizar_cliente()
    if(opc == "3"): eliminar_cliente()
    if(opc == "4"): listar_clientes()
    if(opc == "5"): 
        print("Saliendo...")
        quit()
    menu()
    
def main():
    db.createDB()
    while True: 
        if login(): break
        else: print("Error: Intente de nuevo")
    os.system("clear")
    menu()

if __name__ == "__main__":
    main()