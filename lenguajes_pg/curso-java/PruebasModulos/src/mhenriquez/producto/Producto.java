package mhenriquez.producto;

import mhenriquez.descuentoProducto.Descuento;

public class Producto {
	private static int codigo_siguiente = 0;
	private int codigo;
	private double precio;
	private String nombre;
	
	public Producto() {
		codigo_siguiente++;
		this.codigo = codigo_siguiente;
	}
	
	public int getCodigo() {
		return codigo;
	}
	
	public double getPrecio() {
		return precio;
	}
	
	public String getNombre() {
		return nombre;
	}
	
	public double getDescuento() {
		return Descuento.calcularDescuento(this.precio);
	}
	
	public void setPrecio(double precio) {
		this.precio = precio;
	}
	
	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
}
