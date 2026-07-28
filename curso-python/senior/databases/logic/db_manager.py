import sqlite3
from core.settings import DB_PATH
from contextlib import closing # Cierra los objetos de conexión

class DBManager:
    _query_drop   = "DROP TABLE IF EXISTS productos"
    _query_create = """
    CREATE TABLE IF NOT EXISTS productos (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nombre_articulo VARCHAR(255),
        seccion VARCHAR(255),
        precio DOUBLE(16,2)
    )
    """
    _query_inster = """
    INSERT INTO productos (nombre_articulo, seccion, precio) 
    VALUES
    ("BALÓN", "DEPORTES", 15)
    """

    # ----------------------------------------- Static funcionales no saben que pertenecen a la clase
    @staticmethod
    def probar_conexion() -> None:
        try:
            # Casteamos DB_PATH a string porque sqlite3 nativo a veces se queja de los objetos Path
            conn = sqlite3.connect(DB_PATH)

            print(f"✅ Conexión exitosa a la base de datos en:\n{DB_PATH}")

            conn.close() 
        except sqlite3.Error as e:
            print(f"❌ Error al conectar con SQLite: {e}")

    # ----------------------------------------- Static de clase, pueden usar cls para referenciar a la clase y sus propiedades
    @classmethod
    def insertar_registros(cls) -> None:
        try:
            with closing(sqlite3.connect(DB_PATH)) as conn:
                with conn:
                    cursor = conn.cursor()

                    cursor.execute(cls._query_inster)

                    cursor.close()

            print(f"✅ Registro insertado correctamente")
        except sqlite3.Error as e:
            print(f"❌ Error de base de datos: {e}")

    @classmethod
    def borrar_db(cls) -> None:
        try:
            with closing(sqlite3.connect(DB_PATH)) as conn:
                with conn:
                    cursor = conn.cursor()

                    cursor.execute(cls._query_drop)

                    cursor.close()

            print(f"✅ Base de datos borrada exitosamente")
        except sqlite3.Error as e:
            print(f"❌ Error de base de datos: {e}")

    @classmethod
    def crear_db_open_close(cls) -> None:
        try:
            conn = sqlite3.connect(DB_PATH)

            cursor = conn.cursor()

            cursor.execute(cls._query_create)

            # Confirmar cambios | conn.rollback() para revertirlos, con width se hace solo
            conn.commit()

            cursor.close()
            conn.close()

            print("✅ Tabla 'productos' verificada/creada con éxito.")
        except sqlite3.Error as e:
            print(f"❌ Error de base de datos: {e}")

    @classmethod
    def crear_db_closing_with(cls) -> None:
        try:
            # 1. 'closing' garantiza que conn.close() se ejecute siempre, pase lo que pase
            with closing(sqlite3.connect(str(DB_PATH))) as conn:
                # 2. 'with conn' garantiza el conn.commit() o rollback() de la transacción
                with conn:
                    cursor = conn.cursor()

                    cursor.execute(cls._query_create)
                    
                    # En SQLite no es estrictamente necesario cerrar el cursor si cierras la
                    # conexión inmediatamente después, pero es una excelente práctica de higiene:
                    cursor.close()
                    
            print("✅ Tabla 'productos' verificada/creada con éxito.")
        except sqlite3.Error as e:
            print(f"❌ Error de base de datos: {e}")