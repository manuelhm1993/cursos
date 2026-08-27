package estructurasControlFlujo.bucles.indeterminados;

import javax.swing.JOptionPane;

public class CalcularPesoIdeal {

	public static void main(String[] args) {
		/* Calcular el peso ideal solicitando género y peso en cm
		 * Hombre = 180cm - 110 = 70Kg
		 * Mujer  = 160cm - 120 = 40Kg
		 * */
		
		String genero = getGenero();
		int estatura = getEstatura(); 
		
		calcularPeso(genero, estatura);
	}
	
	public static void calcularPeso(String genero, int estatura) {
		int pesoIdeal = estatura - ((genero.equals("M")) ? 110 : 120);
		
		JOptionPane.showMessageDialog(null, String.format(
			"Para género %s y altura %dcm, su peso ideal es %dkg", 
			(genero.equals("M")) ? "masculino" : "femenino", 
			estatura, pesoIdeal)
		);
	}
	
	public static String getGenero() {
		String genero;
		boolean respuesta = false;
		
		do {
			genero = JOptionPane.showInputDialog("Ingrese su género (M/F)").toUpperCase();
			
			respuesta = genero.equals("M") || genero.equals("F");
			
			if(!respuesta) {
				JOptionPane.showMessageDialog(null, "El género debe ser 'M' ó 'F'");
			}
			
		} while(!respuesta);
		
		return genero;
	}

	public static int getEstatura() {
		int estatura = 0;
		boolean respuesta = false;
		
		while(!respuesta) {
			estatura = Integer.parseInt(JOptionPane.showInputDialog("Ingrese su altura en cm"));
			
			respuesta = estatura >= 50 && estatura <= 220;
			
			if(!respuesta) {
				JOptionPane.showMessageDialog(null, "La estatura debe estar entre [50-220]");
			}
			
		}
		
		return estatura;
	}
}
