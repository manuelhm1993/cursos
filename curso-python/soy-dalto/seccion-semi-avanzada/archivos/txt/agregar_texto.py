from ..config.paths import ARCHIVO_TXT_PATH

# Abrir el archivo, en modo append
with open(ARCHIVO_TXT_PATH, encoding="UTF-8", mode="a") as archivo:
    # Sobreescribe el archivo si está en modo 'w', agrega texto si está en modo 'a'
    for i in range(1, 6):
        archivo.write(f"\n- Línea {i} agregada")