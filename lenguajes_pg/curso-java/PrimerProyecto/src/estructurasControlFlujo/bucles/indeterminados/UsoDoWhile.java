package estructurasControlFlujo.bucles.indeterminados;

import javax.swing.JOptionPane;

public class UsoDoWhile {

	public static void main(String[] args) {
		int numeroSecreto = (int)(Math.random() * 100); // [0-99]
		int intentos = 0, entrada = 0;
		
		// En caso numeroSecreto sea 0 el do-while se asegura que primero se ejecuta y luego se lee la condición
		do {
			entrada = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número [0-99]: "));
			
			intentos++;
			
			if(entrada == numeroSecreto) break;
			
			JOptionPane.showMessageDialog(
				null, 
				(entrada > numeroSecreto) 
				? "Ingrese un número menor" 
				: "Ingrese un número mayor"
			);
		} while(entrada != numeroSecreto);
		
		JOptionPane.showMessageDialog(
			null, 
			String.format("¡Felicidades! Adivinaste el número en %d intentos", intentos)
		);
	}

}
