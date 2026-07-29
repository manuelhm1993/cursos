from core.settings import DB_USUSARIOS

import sqlite3

class DBManager:
    _instancia: DBManager     = None  # Aquí guardaremos el objeto único

    # __new__ se ejecuta ANTES de __init__
    def __new__(cls) -> DBManager:
        try:
            if cls._instancia is None:
                # 1. Si no existe, creamos la instancia en RAM por primera y única vez
                cls._instancia = super().__new__(cls)
                
                # 2. Abrimos la conexión física a SQLite
                # check_same_thread=False es vital en Tkinter si usas eventos asíncronos
                cls._instancia._conn = sqlite3.connect(DB_USUSARIOS, check_same_thread=False)

                print("Conexión creada")
            else:
                print("Conexión activa")
        except sqlite3.Error as e:
            print("Error", f"❌ Error de base de datos: {e}")

        return cls._instancia

    # Se inyectó la propiedad _conn en el objeto
    def get_conexion(self) -> sqlite3.Connection | None:
        return self._conn