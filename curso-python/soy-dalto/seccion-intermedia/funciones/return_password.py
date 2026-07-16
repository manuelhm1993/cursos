from random import randint

# Crear una función con retorno de valor
def crear_contrasenia_random(num):
    chars = "abcdefghijklmnñopqrstuvwxyz"
    
    num_entero = str(num)
    num = int(num_entero[0])
    
    c1 = num - randint(1, 9)
    c2 = num
    c3 = num - randint(1, 9)

    password = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * randint(2, 10)}"

    # Empaquetando una tupla
    return (password, num)

# Desempaquetando una tupla
password, primer_numero = crear_contrasenia_random(850)

# Mostrando resultados
print(f"La contraseña nueva es: {password}")
print(f"El número utilizado para crearla fue: {primer_numero}")