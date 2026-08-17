package fundamentos.string;

import java.text.MessageFormat;

public class UsoString {

	public static void main(String[] args) {
		String nombre1 = "Manuel";
		String nombre2 = "Sugey";
		
		// Forma de comparar objetos
		System.out.println(nombre1.equals(nombre2));
	}
	
	public static void mostrarPosicionesABCIniciales(String nombre1, String nombre2) {
		String abecedario = "";
		
		for(int i=65;i<91;i++) {
			abecedario += ((char)i);
		}
		
		String mensaje = String.format("Las iniciales de los nombres %s y %s forman el número %d%d", 
				nombre1, nombre2, 
				devolverPosicionABCInicial(abecedario, nombre1.toUpperCase().charAt(0)),
				devolverPosicionABCInicial(abecedario, nombre2.toUpperCase().charAt(0)));
		
		System.out.println(mensaje);
	}
	
	private static int devolverPosicionABCInicial(String abecedario, char inicial) {
		int i = 0;
		int letrasAbecedario = abecedario.length();
		
		while(abecedario.charAt(i) != inicial && i < letrasAbecedario) {
			i++;
		}
		
		return i + 1;
	}
	
	public static void usoLengthYFormatos(String nombre) {
		int longitud = nombre.length();
		
		// Diferentes maneras de mostrar un mensaje concatenado
		String mensaje = "";
		
		mensaje = "El nombre " + nombre + " tiene " + longitud + " letras.";
		
		System.out.println(mensaje);
		
		mensaje = String.format("El nombre %s tiene %d letras.", nombre, longitud);
		
		System.out.println(mensaje);
		
		mensaje = MessageFormat.format("El nombre {0} tiene {1} letras.", nombre, longitud);
		
		System.out.println(mensaje);
	}
}
