
while True:
    try:
        print("Calculadora")
        print("(1).- Sumar ")
        print("(2).- Restar")
        print("(3).- Multiplicar")
        print("(4).- Dividir")
        print("(5).- Salir")

        op = int(input("Ingrese una opcion valida del 1 al 5: "))
        
        if op == 5:
            print("Saliendo del programa...")
            break

        elif op == 1:
            num1 = int(input("Ingresa el primer numero: "))
            num2 = int(input("Ingresa el segundo numero: "))
            resultado = num1 + num2
            print(f"El resultado de la suma es {resultado}")

        elif op == 2:
            num1 = int(input("Ingresa el primer numero: "))
            num2 = int(input("Ingresa el segundo numero: "))
            resultado = num1 - num2
            print(f"El resultado de la resta es {resultado}")

        elif op == 3:
            num1 = int(input("Ingresa el primer numero: "))
            num2 = int(input("Ingresa el segundo numero: "))       
            resultado = num1 * num2
            print(f"El resultado de la multiplicacion es {resultado}")

        elif op == 4:
            num1 = int(input("Ingresa el primer numero: "))
            num2 = int(input("Ingresa el segundo numero: "))
            resultado = num1 / num2
            print(f"El resultado de la division es {resultado}")  

        else:
            print("Debes ingresar solo un numero entre 1 y 5!!")

    except ValueError:
        print("Solo debes ingresar numeros enteros!!")

    