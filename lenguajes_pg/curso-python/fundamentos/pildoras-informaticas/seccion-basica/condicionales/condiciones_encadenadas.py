salario_presidente = float(input("Ingrese el salario del presidente: "))
print(f"El salario del presidente es: {salario_presidente}")

salario_director = float(input("Ingrese el salario del director: "))
print(f"El salario del director es: {salario_director}")

salario_jefe_area = float(input("Ingrese el salario del jede de área: "))
print(f"El salario del jede de área es: {salario_jefe_area}")

salario_administrador = float(input("Ingrese el salario del administrador: "))
print(f"El salario del administrador es: {salario_administrador}")

# Concatenación de condiciones
if salario_administrador < salario_jefe_area < salario_director < salario_presidente:
    print("Auditoría correcta")
else:
    print("Hay disparidad en los salarios")