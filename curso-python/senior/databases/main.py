from logic.db_manager import DBManager

if __name__ == "__main__":
    # Controlador
    balon_venezolano = ("Balón", "Depordes", 15)
    nuevo_inventario = [
        ("Camiseta", "Depordes", 10),
        ("Jarrón", "Cerámica", 90),
        ("Camión", "Juguetería", 20),
    ]

    # Controlador & Modelo
    DBManager.borrar_db()
    DBManager.crear_db_closing_with()
    DBManager.insertar_registro(*balon_venezolano)
    DBManager.insetar_multiples_registros(nuevo_inventario)
    productos = DBManager.select_all_productos()

    # Vista
    for producto in productos:
        id, nombre, seccion, precio = producto

        print(f"Descripción del artículo {id}: \n- Nombre: {nombre} \n- Sección: {seccion} \n- Precio: {precio}")