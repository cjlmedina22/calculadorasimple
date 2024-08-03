def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: División por cero."

def calculadora():
    while True:
        print("\n-- Calculadora --")
        print("Selecciona la operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        seleccion = input("Ingresa tu opción (1/2/3/4/5): ")

        if seleccion == '5':
            print("Saliendo de la calculadora. ¡Hasta luego!")
            break

        if seleccion in ['1', '2', '3', '4']:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if seleccion == '1':
                print(f"{num1} + {num2} = {sumar(num1, num2)}")
            elif seleccion == '2':
                print(f"{num1} - {num2} = {restar(num1, num2)}")
            elif seleccion == '3':
                print(f"{num1} * {num2} = {multiplicar(num1, num2)}")
            elif seleccion == '4':
                resultado = dividir(num1, num2)
                print(f"{num1} / {num2} = {resultado}")
        else:
            print("Selección no válida. Intenta de nuevo.")

# Ejecutar la calculadora
calculadora()
