from ..config.paths import ARCHIVO_TXT_PATH

# Abrir el archivo, en modo escritura
with open(ARCHIVO_TXT_PATH, encoding="UTF-8", mode="w") as archivo:
    # Sobreescribe el archivo
    # archivo.write("MHenriquez pronto será una empresa reconocida.")

    # Escribe el texto de un iterable
    archivo.writelines(("Acabas de escribir un archivo con Python", "\n", "Felicidades.", "\n"))

    # Se puede usar varias veces para añadir texto
    archivo.writelines(("Prueba de añadir", "\n", "Felicidades."))