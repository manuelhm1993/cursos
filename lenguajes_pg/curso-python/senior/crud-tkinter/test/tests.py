from pathlib import Path

DB_PATH = Path(__file__).resolve().parent.parent / "data/usuarios.db"

def validar_tabla_db():
    import sqlite3

    # Conectar a la base de datos (o crearla)
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()

    # Nombre de la tabla que deseas buscar
    nombre_tabla = "usuarios"

    # Consultar la tabla del sistema sqlite_master
    cursor.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?;",
        (nombre_tabla,),
    )

    # Obtener el resultado
    resultado = cursor.fetchone()

    if resultado:
        print(f"La tabla '{nombre_tabla}' sí existe.")
    else:
        print(f"La tabla '{nombre_tabla}' no existe.")

    conexion.close()


def validar_archivo():
    print("El archivo existe" if DB_PATH.is_file() else "El archivo no existe")

def barra_menu_botones():
    import tkinter as tk

    root = tk.Tk()
    root.geometry("300x200")

    # 1. Creamos un Frame que actuará como nuestra barra de menú personalizada
    frame_barra = tk.Frame(root, bg="lightgray", relief="raised", bd=1)
    frame_barra.pack(side="top", fill="x")

    # 2. Creamos un Menubutton y lo metemos en nuestro Frame
    boton_archivo = tk.Menubutton(frame_barra, text="Archivo", activebackground="gray")
    boton_archivo.pack(side="left", padx=5)

    # 3. Creamos el menú que se desplegará de ese botón
    menu_archivo = tk.Menu(boton_archivo, tearoff=0)
    menu_archivo.add_command(label="Nuevo")
    menu_archivo.add_separator()
    menu_archivo.add_command(label="Salir", command=root.quit)

    # 4. Enlazamos el menú al botón
    boton_archivo.config(menu=menu_archivo)

    root.mainloop()

validar_tabla_db()