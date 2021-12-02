



print("\nBienvenidos\n")
print("Te pediremos dos numeros, para que puedas realizar la siguientes operaciones\n ")



def menu_principal ():
    print("Menu Principal \n" +
    "1. Suma \n" +
    "2. Resta \n" +
    "3. Multiplicacion \n" +
    "4. Divison \n" +
    "Elija una Opcion :) \n")

def ingrese_opcion():
    return int(input())


menu_principal()
option = ingrese_opcion()

print("Digite su primer valor: ")
n1 = float(input())
print("Digite su segundo valor: ")
n2 = float(input())

def numeros(n1, n2):

    return

def suma_numero(n1, n2):
    numeros(n1, n2)
    result = n1 + n2
    print("El resultado de la suma es: ",result)

def resta_numero(n1, n2):
    numeros(n1, n2)
    result = n1 - n2
    print("El resultado de la resta es: ", result)

def multi_numero(n1, n2):
    numeros(n1, n2)
    result = n1 * n2
    print("El resultado de la multiplicacion es: ", result)

def divi_numero(n1, n2):
    if n2 == 0:
        print("No se puede dividir entre 0")
    else:
        result = n1 / n2
        print("El resultado de la division es " + str(result))



if option == 1:
    suma_numero(n1, n2)

elif option == 2:
    resta_numero(n1, n2)

elif option == 3:
    multi_numero(n1, n2)

elif option == 4:
    divi_numero(n1, n2)




