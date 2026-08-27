package estructurasControlFlujo.bucles.indeterminados;

import javax.swing.JOptionPane;

public class UsoWhile {

	public static void main(String[] args) {
		String password = "Sugey", input;
		boolean login = false;
		
		while(!login) {
			input = JOptionPane.showInputDialog("Ingrese su contraseña: ");
			
			login = input.equals(password);
			
			JOptionPane.showMessageDialog(null, (login) ? "Acceso concedido" : "Contraseña incorrecta");
		}
	}

}
