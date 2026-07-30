frase = input("Dime una frase y te calculo cuánto tardarías si tuvieras que decirla: ")

palabras_separadas = frase.split()

c_palabras = len(palabras_separadas)

print(f"Dijiste {c_palabras} palabras, por lo que tardarías aproximadamente {c_palabras / 2:.2f} segundos en decirla.")
print(f"Dalto lo diría en {c_palabras / 2 * 1.3:.2f} segundos.")

if c_palabras > 120:
    print("¡Esa frase es muy larga! Dalto tardaría más de 1 minuto en decirla.")