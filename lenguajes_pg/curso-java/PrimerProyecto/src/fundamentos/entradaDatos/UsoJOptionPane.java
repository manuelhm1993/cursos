package fundamentos.entradaDatos;

import javax.swing.JOptionPane;

public class UsoJOptionPane {

	public static void main(String[] args) {
		String nombre = JOptionPane.showInputDialog("Ingrese su nombre");
		int edad = Integer.parseInt(JOptionPane.showInputDialog("Ingrese su edad"));
		double salario = Double.parseDouble(JOptionPane.showInputDialog("Ingrese su salario"));
		
		String response = String.format(
			"Bienvenido %s. El año que viene tendrás %d años. Su salario es %g", 
			nombre, ++edad, salario
		);
		
		JOptionPane.showMessageDialog(null, response);
	}

}
