import os
import helpers
import database as db

def iniciar():
    while True:
        helpers.limpiar_pantalla()

        print("===========================")
        print("   Bienvenido al Gestor   ")
        print("===========================")
        print("[1] Listar los clientes")
        print("[2] Buscar un cliente")
        print("[3] Añadir un cliente")
        print("[4] Modificar un cliente")
        print("[5] Borrar un cliente")
        print("[6] Cerrar el gestor")
        print("===========================")

        opcion = input ("> ")

        helpers.limpiar_pantalla()

        match opcion:

            case "1":
                print ("Listando los clientes...\n")
                for cliente in db.Clientes.lista:
                    print(cliente)

            case "2":
                print ("Buscando un cliente...\n")
                dni = helpers.leer_texto(3,3,"DNI (2 int y 1 char)").upper()
                cliente = db.Clientes.buscar(dni)
                print (cliente) if cliente else print("Cliente no encontrado.")

            case "3":
                print ("Añadiendo un cliente...\n")
                dni = helpers.leer_texto(3,3,"DNI (2 int y 1 char)").upper()
                nombre = helpers.leer_texto(2,30,"Nombre (2 a 30 chars)").capitalize()
                apellido = helpers.leer_texto(2,30,"Apellido (2 a 30 chars)").capitalize()
                db.Clientes.crear(dni,nombre,apellido)
                print("Cliente añadido correctamente.")

            case "4":
                print ("Modificando un cliente...\n")
                dni = helpers.leer_texto(3,3,"DNI (2 int y 1 char)").upper()
                cliente = db.Clientes.buscar(dni)

                if cliente:
                    nombre = helpers.leer_texto(2,30, f"Nombre (2 a 30 chars) [{cliente.nombre}]").capitalize()
                    apellido = helpers.leer_texto(2,30, f"Apellido (2 a 30 chars) [{cliente.apellido}]").capitalize()
                    db.Clientes.modificar(dni, nombre, apellido)
                    print("Cliente modificado correctamente.")
                else:
                    print("Cliente no encontrado.")

            case "5":
                print ("Borrando un cliente...\n")
                dni = helpers.leer_texto(3,3,"DNI (2 int y 1 char)").upper()
                print ("Cliente borrado correctamente.") if db.Clientes.borrar(dni) else print("Cliente no encontrado.")

            case "6":
                print ("Saliendo...\n")
                break

            case _:
                print("La opcion ingresada es incorrecta. Por favor, ingrese un número válido.")

        input("\nPresiona ENTER para continuar...")