def dividir() -> None:
    while True:
        try:
            op1 = float(input("Ingrese el operador 1: "))
            op2 = float(input("Ingrese el operador 2: "))

            resultado = op1 / op2

            print(f"{op1} / {op2} = {resultado}")
            break
        except ValueError as e:
            print("Error. Introduce un valor numérico")
        except ZeroDivisionError as e:
            print("Error. No se puede dividir por cero")
            break

    print("Operación concluida.")

dividir()