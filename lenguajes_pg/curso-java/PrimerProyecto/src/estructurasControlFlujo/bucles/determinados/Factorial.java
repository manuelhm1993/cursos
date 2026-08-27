package estructurasControlFlujo.bucles.determinados;

import javax.swing.JOptionPane;

public class Factorial {

	public static void main(String[] args) {
		long numero = Long.parseLong(JOptionPane.showInputDialog("Ingrese un número"));
		
		System.out.println(String.format("%d! = %d", numero, factorial(numero)));
		// System.out.println(String.format("%d! = %d", numero, factorialRecursiva(numero)));
	}

	public static long factorial(long numero) {
		long resultado = 1L;
		
		for(int i = 1; i <= numero; i++) {
			resultado *= i;
		}
		
		return resultado;
	}
	
	public static long factorialRecursiva(long numero) {
		return (numero == 0) ? 1 : numero * factorialRecursiva(numero - 1);
	}
}
