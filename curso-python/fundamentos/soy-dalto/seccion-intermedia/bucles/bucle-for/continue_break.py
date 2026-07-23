frutas = ["Parchita", "Manzana", "Ciruela", "Pera", "Naranja", "Durazno", "Mango"]

for fruta in frutas:
    # Al llegar a la instrucción continue termina esta iteración y sigue a la siguiente
    if fruta == "Ciruela":
        continue

    print(f"Me voy a comer una: {fruta}")
else:
    print()

for fruta in frutas:
    print(f"Me voy a comer una: {fruta}")

    # Terminar el bucle con break, al usar break, ni siquiera ejecuta un else
    if fruta == "Pera":
        break

print("Fin del programa")