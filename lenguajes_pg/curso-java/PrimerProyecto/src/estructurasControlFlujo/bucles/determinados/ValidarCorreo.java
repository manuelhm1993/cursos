package estructurasControlFlujo.bucles.determinados;

import javax.swing.JOptionPane;

public class ValidarCorreo {

	public static void main(String[] args) {
		String correo = JOptionPane.showInputDialog("Ingrese su correo");
		int n_caracteres = correo.length();
		int arroba = 0;
		boolean punto = false;
		
		for(int i=0;i<n_caracteres;i++) {
			if(correo.charAt(i) == '@') {
				arroba++;
			}
			
			if(correo.charAt(i) == '.') {
				punto = true;
			}
		}
		
		System.out.println((arroba == 1 && punto) ? "Correo válido" : "Correo inválido");
	}

}
