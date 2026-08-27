package estructurasControlFlujo.bucles.indeterminados;

import javax.swing.JOptionPane;

public class NumeroMagico {

	public static void main(String[] args) {
		int numeroSecreto = (int)((Math.random() * 100) + 1);
		int intentos = 0, entrada = 0;
		
		while(entrada != numeroSecreto) {
			entrada = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número [1-100]: "));
			
			intentos++;
			
			if(entrada == numeroSecreto) break;
			
			JOptionPane.showMessageDialog(
				null, 
				(entrada > numeroSecreto) 
				? "Ingrese un número menor" 
				: "Ingrese un número mayor"
			);
		}
		
		JOptionPane.showMessageDialog(
			null, 
			String.format("¡Felicidades! Adivinaste el número en %d intentos", intentos)
		);
	}

}
