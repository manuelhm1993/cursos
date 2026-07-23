def contar_caracteres(frase, bucle=False):
    contador = 0
    
    if bucle:
        for i in frase:
            if i == ' ':
                continue

            contador += 1
    else:
        contador = len(frase) - frase.count(" ")

    return contador

nombre = "Píldoras Informáticas"

print(f"El nombre {nombre} tiene {contar_caracteres(nombre)} sin contar espacios")
print(f"El nombre {nombre} tiene {contar_caracteres(nombre, True)} sin contar espacios")