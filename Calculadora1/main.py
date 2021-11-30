
print("\nBienvenidos\n")
print("Te pediremos dos numeros, para que puedas realizar la siguientes operaciones\n ")



menuprincipal = int(input("Menu Principal \n" +
                    "1. Suma \n" +
                    "2. Resta \n" +
                    "3. Multiplicacion \n" +
                    "4. Divison \n" +
                    "Elija una Opcion :) \n"))


while menuprincipal != 0:
    if menuprincipal == 1:
        num1 = int(input("Digite el primer numero: "))
        num2 = int(input("Digite el segundo numero: "))
        result = num1 + num2
        print("El resultado de la suma es: ", result)
    elif menuprincipal == 2:
        num3 = int(input("Digite el primer numero: "))
        num4 = int(input("Digite el segundo numero: "))
        result1 = num3 - num4
        print("El resultado de la resta es: ", result1)
    elif menuprincipal == 3:
        num5 = int(input("Digite el primer numero: "))
        num6 = int(input("Digite el segundo numero: "))
        result2 = num5 * num6
        print("El resultado de la multiplicacion es: ", result2)
    elif menuprincipal == 4:
        num7 = float(input("Digite el primer numero: "))
        num8 = float(input("Digite el primer numero: "))
        result3 = num7 / num8
        if num8 == 0:
            print("El divisor no puede ser igual a cero \n"+
            "Utilice otro valor")
        else:
            print("el resultado de la division es: ", result3)
    else:
        print("Espero haya sido de tu ayuda")




