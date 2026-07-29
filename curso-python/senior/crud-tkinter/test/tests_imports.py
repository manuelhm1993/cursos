from pathlib import Path

import sys

# 1. Calculamos la ruta de la carpeta padre ('crud-tkinter') y la agregamos al sistema
BASE_DIR = str(Path(__file__).resolve().parent.parent)

# Se puede solucionar usando: py -m crud-tkinter.test.tests_imports y ruta relativa ..core.senttings pero el '-' da error
sys.path.append(BASE_DIR)

# 2. Ahora hacemos una importación ABSOLUTA (sin los dos puntos iniciales)
from core.settings import DB_USUSARIOS

import sqlite3

if __name__ == "__main__":

    class SQLiteSingleton:
        _instancia = None  # Aquí guardaremos el objeto único
        _conexion = None   # Aquí guardaremos la conexión abierta

        # __new__ se ejecuta ANTES de __init__
        def __new__(cls):
            if cls._instancia is None:
                # 1. Si no existe, creamos la instancia en RAM por primera y única vez
                cls._instancia = super().__new__(cls)
                
                # 2. Abrimos la conexión física a SQLite
                # check_same_thread=False es vital en Tkinter si usas eventos asíncronos
                cls._instancia._conexion = sqlite3.connect(str(DB_USUSARIOS), check_same_thread=False)
                print("⚙️ [Sistema] Construyendo la ÚNICA conexión a la Base de Datos.")
            else:
                print("⚡ [Sistema] Reutilizando conexión existente en memoria.")
                
            return cls._instancia

        def get_conexion(self):
            """Método público para pedir prestado el cable de conexión"""
            return self._conexion

    # ==========================================
    # Demostración del Singleton en acción
    # ==========================================

    # Módulo A (ej. main.py) pide una conexión
    db1 = SQLiteSingleton() 
    conexion_a = db1.get_conexion() # Imprime: Construyendo la ÚNICA conexión...

    # Módulo B (ej. user_controller.py) pide una conexión 5 segundos después
    db2 = SQLiteSingleton()
    conexion_b = db2.get_conexion() # Imprime: Reutilizando conexión existente...

    # Prueba de fuego (Demostración de memoria RAM)
    print(db1 is db2) # ✅ TRUE. Son exactamente el mismo objeto. No abriste 2 archivos.