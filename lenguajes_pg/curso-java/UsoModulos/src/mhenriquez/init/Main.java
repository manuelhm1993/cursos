package mhenriquez.init;

import mhenriquez.producto.Producto;

public class Main {

	public static void main(String[] args) {
		/**
		 * Este proyecto utiliza el proyecto PruebasModulos como dependencia, esto se especifica de la siguiente manera:
		 * 1. Click derecho/propiedades sobre el proyecto actual
		 * 2. Java Build Path/Project
		 * 3. Modulepath y agregar el módulo correspondiente/proyecto correspondiente
		 * 4. El módulo debe estar previamente configurado, es como el __all__ de los paquetes de python
		 * 5. El módulo debe ser requerido en el proyecto actual como en php
		 */
		
		Object[][] productos = {
			{new Producto(), new Producto(), new Producto()},
			{15000.0, 25000.0, 1200.0},
			{"Silla gamer", "Laptop de diseño", "Mouse inalámbrico"}
		};
		
		int items = productos[0].length;
		
		for(int i=0; i<items; i++) {
			Producto producto = (Producto) productos[0][i];
			
			producto.setPrecio((double)productos[1][i]);
			producto.setNombre((String)productos[2][i]);
		}
		
		for(int i=0; i<items; i++) {
			Producto producto = (Producto) productos[0][i];
			
			System.out.println("Producto: "
				+ "\n- Código: " + producto.getCodigo()
				+ "\n- Nombre: " + producto.getNombre()
				+ "\n- Precio: " + producto.getPrecio()
				+ "\n- Con descuento: " + producto.getDescuento()
			);
		}
	}

}
