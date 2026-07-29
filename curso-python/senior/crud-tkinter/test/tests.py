import tkinter as tk
import sqlite3

from pathlib import Path

def validar_archivo():
    archivo = Path(__file__).resolve().parent.parent / "data/usuarios.db"

    print("El archivo existe" if archivo.is_file() else "El archivo no existe")

def barra_menu_botones():
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

class SQLiteSingleton:
    _instancia: SQLiteSingleton   = None  # Aquí guardaremos el objeto único
    _conexion: sqlite3.Connection = None  # Aquí guardaremos la conexión abierta

    # __new__ se ejecuta ANTES de __init__
    def __new__(cls) -> SQLiteSingleton:
        if cls._instancia is None:
            # 1. Si no existe, creamos la instancia en RAM por primera y única vez
            cls._instancia = super().__new__(cls)
            
            # 2. Abrimos la conexión física a SQLite
            # check_same_thread=False es vital en Tkinter si usas eventos asíncronos
            cls._instancia._conexion = sqlite3.connect("usuarios.db", check_same_thread=False)
            print("⚙️ [Sistema] Construyendo la ÚNICA conexión a la Base de Datos.")
        else:
            print("⚡ [Sistema] Reutilizando conexión existente en memoria.")
            
        return cls._instancia

    def get_conexion(self) -> sqlite3.Connection:
        return self._conexion