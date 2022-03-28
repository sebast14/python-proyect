
import pandas as pd


numeros_celular = []

def add():
    per=[]
    per.append(input("Nombre : "))
    per.append(input("Telefono: "))
    per.append(input("Correo: "))
    per.append(input("Cumpleaños: "))
    return per

def listar():
    for per in numeros_celular:
        print("Nombre: ", per[0])
        print("Telefono: ", per[1])
        print("Correo: ", per[2])
        print("Cumpleaños: ", per[3])
        print("º")


dtmp = pd.read_csv("contactos.agenda")
tmp = dtmp.values.tolist()
for lin in tmp:
     t = []
     t.append(lin[1])
     t.append(lin[2])
     t.append(lin[3])
     t.append(lin[4])
     numeros_celular.append(t)

def modificar():
    posicion=input("ingrese la posicion en la que se encuentra su contacto")
    if posicion == "1":
        numeros_celular[0] = add()
        df = pd.DataFrame(numeros_celular, columns=["Nombre", "Telefono", "Correo", "Cumpleaños"])
        df.to_csv("contactos.agenda")
        agenda()

#def eliminar_contacto():
     #   eliminar_contacto = input("Nombre a eliminar: ")

      #  add_archivo = open("contactos.agenda")
       # t = []
        #for linea in add_archivo:
         #   valores = linea.strip().split(',')
          #  t.append(valores)
        #add_archivo.close()




def agenda():
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
        listar()
        agenda()




    if option == "3":
        numeros_celular.append(add())
        print("El numero de celular fue agragado con exito.")
        agenda()

    if option == "4":
        modificar()
        print("El contacto fue modificado con exito.")
        agenda()

    if option == "5":
        eliminar_contacto()
        print("Su contacto a sido eliminado con exito")
        agenda()

    if option == "6":

        df = pd.DataFrame(numeros_celular, columns=["Nombre", "Telefono", "Correo", "Cumpleaños"])
        df.to_csv("contactos.agenda")



agenda()
















