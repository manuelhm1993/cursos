package mhenriquez.descuentoProducto;

public class Descuento {
	
	// Devuelve el precio con un 15% de descuento
	public static double calcularDescuento(double precio) { 
		return precio - (precio * 0.15);
	}
}
