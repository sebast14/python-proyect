
numeros_celular = {"Camilo": 3154203143,
                       "David": 3214567894,
                       "Sebastian": 3145678431,
                       "Juan": 3208184605}
agenda = True

while agenda:
    print("\n------AGENDA------")
    print("1) Mis contactos.")
    print("2) Buscar contacto.")
    print("3) Agregar nuevo contacto.")
    print("4) Editar contacto.")
    print("5) Eliminar contacto.")
    print("6) Salir.")

    option = ""
    while option not in ("1", "2", "3", "4", "5", "6"):
        option = input("\nDijite la opcion deseada \n-> ")

    if option == "1":
        print(numeros_celular)

    if option == "2":
        nombre = input("\nNombre: ")
        if nombre not in numeros_celular:
            print("Ese contacto no esta registrado.")
            print("¿Desea hacerlo? Si es asi, pulse la opcion 3.")
        else:
            cel = numeros_celular[nombre]
            print(nombre, ":", cel)

    elif option == "3":
        nombre = input("\nIngrese el nombre de su nuevo contacto: ")
        if nombre in numeros_celular:
            print("Ese contacto ya esta registrado.")
        else:
            cel = int(input("Ingrese el numero: "))
            numeros_celular[nombre] = cel
            print("El numero de celular fue agragado con exito.")

    elif option == "4":
        nombre = input("\nNombre del contacto que desea modificar: ")
        if nombre not in numeros_celular:
            print("Numero inexistente.")
            print("¿Desea registrarlo? Si es asi, pulse la opcion 3.")
        else:
            cel = int(input("Dijite el nuevo numero: "))
            numeros_celular[nombre] = cel
            print("El numero ha sido modificado con exito.")

    elif option == "5":
        nombre = input("Nombre: ")
        if nombre not in numeros_celular:
            print("Ese contacto no esta registrado")
            print("¿Desea registrarlo? Si es asi, pulse la opcion 3.")
        else:
            del numeros_celular[nombre]
            print("El numero ha sido eliminado. ")

    elif option == "6":
        agenda = exit()



























