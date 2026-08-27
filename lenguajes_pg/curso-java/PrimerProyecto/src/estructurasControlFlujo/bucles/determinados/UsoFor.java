package estructurasControlFlujo.bucles.determinados;

import javax.swing.JOptionPane;

public class UsoFor {

	public static void main(String[] args) {
		// Validar un correo
		String correo = JOptionPane.showInputDialog("Ingrese su correo");
		int n_caracteres = correo.length();
		boolean arroba = false;
		
		for(int i=0;i<n_caracteres;i++) {
			if(correo.charAt(i) == '@') {
				arroba = true;
				break;
			}
		}
		
		System.out.println((arroba) ? "Correo válido" : "Correo inválido");
	}

}
