print("Bienvenido.\n")
print("Se le ha asignado un usuario y una contraseña que será mostrada a continuación: \n\n" +
      "Usuario: electivaprogramacion@python.com \n"
      "Contraseña: sebastian2019\n")

user = "electivaprogramacion@python.com"
password = "sebastian2019"


def validation_user():
    return str(input("Digite por favor su usuario: "))


def validation_password():
    return str(input("Ahora digite su contraseña: "))


def user_comp():
    if user == validation_user():
        print("Usuario correcto \n\n")
        password_comp()
    else:
        print("Intentelo de nuevo: ")
        user_comp()


def message_activation():
    print("Felicidades\n"                
          "Has entrado exitosamente")
    exit()


def password_comp():
    if password == validation_password():
        print("Acceso concedido\n\n")
        message_activation()
 
    else:
        print("Intente digitar su contraseña nuevamente: ")
        password_comp()


user_comp()
password_comp()
























    