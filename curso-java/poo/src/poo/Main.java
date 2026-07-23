package poo;

import poo.encapsulacion.Transporte;
import poo.polimorfismo.Director;
import poo.polimorfismo.Empleado;

public class Main {

	public static void main(String[] args) {
		polimorfismo();
	}
	
	public static void polimorfismo() {
		Empleado[] empleados = new Empleado[]{
			new Empleado(), new Empleado(), new Empleado(), 
			new Director(), new Empleado()
		};
		
		
		// Foreach
		for (Empleado empleado : empleados) {
			empleado.trabajar();
			
			//System.out.println(empleado.getClass().getSimpleName());
		}
	}
	
	public static void encapsulacion() {
		Transporte t1 = new Transporte();
		
		t1.setCosto();
		
		System.out.println("El costo del viaje es: " + t1.getCosto());
	}
}
