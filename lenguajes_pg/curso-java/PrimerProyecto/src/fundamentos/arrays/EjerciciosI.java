package fundamentos.arrays;

import javax.swing.JOptionPane;

public class EjerciciosI {

	public static void main(String[] args) {
		String respuesta = JOptionPane.showInputDialog("¿Deseas ver los países o los números aleatorios? [1-2]");
		int opcion = Integer.parseInt(respuesta);
		
		switch(opcion) {
			case 1 -> paisesTurismo(8);
			case 2 -> arrayAleatorios(200);
			default -> JOptionPane.showMessageDialog(null, "Opción no contemplada");
		}
		
	}
	
	public static void paisesTurismo(int elementos) {
		String[] paises = new String[elementos];
		
		int i = 0;
		
		while(i < elementos) {
			paises[i] = JOptionPane.showInputDialog(String.format("Ingrese el país #%d", (i+1)));
			i++;
		}
		
		imprimirArray(paises);
	}
	
	public static void arrayAleatorios(int elementos) {
		Integer[] numeros = new Integer[elementos];
		
		for(int i=0;i<elementos;i++) {
			int nuevoItem = (int)(Math.random() * 100) + 1;
			
			numeros[i] = (i > 99) ? nuevoItem *= 2 : nuevoItem;
		}
		
		imprimirArray(numeros);
	}
	
	private static void imprimirArray(Object[] items) {
		for(var item: items) {
			System.out.println(item);
		}
	}

}
