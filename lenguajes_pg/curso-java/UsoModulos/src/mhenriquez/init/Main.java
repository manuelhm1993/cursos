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
		
		int i = 0;
		
		for(Object objeto: productos[0]) {
			Producto producto = (Producto)objeto;
			
			configurarProducto(producto, (double)productos[1][i], (String)productos[2][i]);
			i++;
			mostrarProductos(producto);
		}
	}
	
	public static void configurarProducto(Producto producto, double precio, String nombre) {
		producto.setPrecio(precio);
		producto.setNombre(nombre);
	}
	
	public static void mostrarProductos(Producto producto) {
		System.out.println("Producto: "
			+ "\n- Código: " + producto.getCodigo()
			+ "\n- Nombre: " + producto.getNombre()
			+ "\n- Precio: " + producto.getPrecio()
			+ "\n- Con descuento: " + producto.getDescuento()
		);
	}

}
