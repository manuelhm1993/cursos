package poo.encapsulacion;

public class Transporte {
	
	public void reservar() {
		System.out.println("Reserva realizada");
	}
	
	public double getCosto() {
		return costo;
	}
	
	public void setCosto() {
		// Cálculos complejos
		costo = calcularCostoTaxi() + calcularCostoMetro();
	}
	
	private double calcularCostoTaxi() {
		// Realiza cálculos
		return 40;
	}
	
	private double calcularCostoMetro() {
		// Realiza cálculos
		return 5;
	}
	

	// -------------------------- Campos de clase
	private int id;
	private int tiempo;
	private double costo;
}
