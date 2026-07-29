from logic.db_manager import DBManager, sqlite3

class UserModel:
    _conn = DBManager().get_conexion()

    _queries = {
        "CREATE": """
            CREATE TABLE usuarios (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nombre_usuario VARCHAR(50),
                password       VARCHAR(16),
                apellido       VARCHAR(50),
                direccion      VARCHAR(100),
                comentarios    TEXT
            )
        """,
        "INSERT": """
            INSERT INTO usuarios (nombre_usuario, password, apellido, direccion, comentarios)
            VALUES 
            (?, ?, ?, ?, ?)
        """,
        "SELECT": "SELECT * FROM usuarios WHERE id = ?",
        "UPDATE": """
            UPDATE usuarios 
            SET nombre_usuario = ?, password = ?, apellido = ?, direccion = ?, comentarios = ?
            WHERE id = ?
        """,
        "DELETE": "DELETE FROM usuarios WHERE id = ?"
    }

    @classmethod
    def crear_tabla_usuarios(cls) -> tuple:
        try:
            cursor = cls._conn.cursor()

            cursor.execute(cls._queries["CREATE"])

            cls._conn.commit()
            cursor.close()

            return ("Éxito", f"Conexión creada exitosamente")
        except sqlite3.OperationalError as e:
            return ("Aviso", f"La conexión ya existe")
        except sqlite3.Error as e:
            return ("Error", f"Error crear la tabla usuarios: {e}")

    @classmethod
    def crear_usuario(cls, usuario: tuple) -> tuple:
        try:
            cursor = cls._conn.cursor()

            cursor.execute(cls._queries["INSERT"], usuario)

            cls._conn.commit()
            registros_afectados = cursor.rowcount
            cursor.close()

            return ("Éxito", f"Inserción realizada exitosamente. Cantidad de registros afectados: {registros_afectados}")
        except sqlite3.Error as e:
            return ("Error", f"Error al crear el usuario {e}")

    @classmethod
    def leer_usuario(cls, usuario_id: tuple) -> tuple:
        try:
            cursor = cls._conn.cursor()

            cursor.execute(cls._queries["SELECT"], usuario_id)

            usuario = cursor.fetchone()

            cursor.close()

            return usuario
        except sqlite3.Error as e:
            return ("Error", f"Error al leer el usuario: {e}")

    @classmethod
    def actualizar_usuario(cls, request: tuple, usuario_id: tuple) -> tuple:
        try:
            cursor = cls._conn.cursor()

            # Desempaquetado de tuplas pythonico
            cursor.execute(cls._queries["UPDATE"], (*request, *usuario_id))

            cls._conn.commit()
            registros_afectados = cursor.rowcount
            cursor.close()

            return ("Éxito", f"Actualización realizada exitosamente. Cantidad de registros afectados: {registros_afectados}")
        except sqlite3.Error as e:
            return ("Error", f"Error al actualizar el usuario: {e}")

    @classmethod
    def borrar_usuario(cls, usuario_id: tuple) -> tuple:
        try:
            cursor = cls._conn.cursor()

            cursor.execute(cls._queries["DELETE"], usuario_id)

            cls._conn.commit()
            registros_afectados = cursor.rowcount
            cursor.close()

            return ("Éxito", f"Borrado realizado exitosamente. Cantidad de registros afectados: {registros_afectados}")
        except sqlite3.Error as e:
            return ("Error", f"Error al borrar el usuario: {e}")