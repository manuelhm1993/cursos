from logic.db_manager import DBManager, sqlite3

class UserModel:
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
    def ultimo_usuario(cls) -> tuple | None:
        conn = cls._obtener_conexion()

        data = {
            "ULTIMO_USUARIO": 
            """
            SELECT * FROM usuarios WHERE id=(
                    SELECT MAX(id) FROM usuarios
                )
            """
        }

        try:
            # Consultar la tabla del sistema sqlite_master
            cursor = conn.execute(data["ULTIMO_USUARIO"])
    
            # Obtener el resultado
            resultado = cursor.fetchone()

            return resultado
        except sqlite3.Error as e:
            return ("Error", f"Error al validar la tabla: {e}")

    @classmethod
    def _validar_conexion_tabla_usuarios(cls, conn: sqlite3.Connection) -> tuple | None:
        data = {
            "SELECT": "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            "CRITERIO": ("usuarios",)
        }

        try:
            # Consultar la tabla del sistema sqlite_master
            cursor = conn.execute(data["SELECT"], data["CRITERIO"])
    
            # Obtener el resultado
            resultado = cursor.fetchone()

            return resultado
        except sqlite3.Error as e:
            return ("Error", f"Error al validar la tabla: {e}")

    @classmethod
    def _obtener_conexion(cls) -> sqlite3.Connection:
        """Helper interno para Lazy Loading. Pide el taxi solo cuando lo necesita."""
        return DBManager().get_conexion()

    @classmethod
    def crear_tabla_usuarios(cls) -> tuple:
        conn = cls._obtener_conexion()
        try:
            # 'with conn' maneja el commit y rollback automáticamente en la transacción
            with conn: 
                conn.execute(cls._queries["CREATE"])
            return ("Éxito", "Conexión creada exitosamente")
        except sqlite3.OperationalError as e:
            return ("Aviso", "La conexión ya existe")
        except sqlite3.Error as e:
            return ("Error", f"Error al crear la tabla usuarios: {e}")

    @classmethod
    def crear_usuario(cls, usuario: tuple) -> tuple:
        conn = cls._obtener_conexion()

        if cls._validar_conexion_tabla_usuarios(conn) is None:
            return ("Aviso", "Primero debe abrir la conexión con la DB")

        try:
            with conn:
                # conn.execute devuelve un cursor temporal, ejecutamos y extraemos rowcount
                cursor = conn.execute(cls._queries["INSERT"], usuario)
                registros_afectados = cursor.rowcount
                
            return ("Éxito", f"Inserción realizada. Registros afectados: {registros_afectados}")
        except sqlite3.Error as e:
            return ("Error", f"Error al crear el usuario {e}")

    @classmethod
    def leer_usuario(cls, usuario_id: tuple) -> tuple:
        conn = cls._obtener_conexion()
        try:
            # Para SELECT no necesitamos 'with' porque no modifica datos (no hay commit)
            cursor = conn.execute(cls._queries["SELECT"], usuario_id)
            usuario = cursor.fetchone()
            return usuario
        except sqlite3.Error as e:
            return ("Error", f"Error al leer el usuario: {e}")

    @classmethod
    def actualizar_usuario(cls, request: tuple, usuario_id: tuple) -> tuple:
        conn = cls._obtener_conexion()
        try:
            with conn:
                cursor = conn.execute(cls._queries["UPDATE"], (*request, *usuario_id))
                registros_afectados = cursor.rowcount
            return ("Éxito", f"Actualización realizada. Registros afectados: {registros_afectados}")
        except sqlite3.Error as e:
            return ("Error", f"Error al actualizar el usuario: {e}")

    @classmethod
    def borrar_usuario(cls, usuario_id: tuple) -> tuple:
        conn = cls._obtener_conexion()
        try:
            with conn:
                cursor = conn.execute(cls._queries["DELETE"], usuario_id)
                registros_afectados = cursor.rowcount
            return ("Éxito", f"Borrado exitoso. Registros afectados: {registros_afectados}")
        except sqlite3.Error as e:
            return ("Error", f"Error al borrar el usuario: {e}")