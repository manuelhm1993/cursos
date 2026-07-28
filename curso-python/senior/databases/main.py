from logic.db_manager import DBManager
from logic.db_controller import DBController

if __name__ == "__main__":
    # Controlador
    seccion = DBController.latin_character_validate("cOnFeccIÖn")

    # Modelo
    productos = DBManager.select_productos_seccion(seccion)

    # Vista
    for producto in productos:
        id, nombre, seccion, precio = producto

        print(f"Descripción del artículo {id}: \n- Nombre: {nombre} \n- Sección: {seccion} \n- Precio: {precio}")

    DBManager.update_producto_id(1, 35)
    DBManager.delete_producto_id(5)

    productos = DBManager.select_all_productos()

    print("*" * 30)
    
    # Vista
    for producto in productos:
        id, nombre, seccion, precio = producto

        print(f"Descripción del artículo {id}: \n- Nombre: {nombre} \n- Sección: {seccion} \n- Precio: {precio}")