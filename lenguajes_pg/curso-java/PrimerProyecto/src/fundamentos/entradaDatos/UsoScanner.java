package fundamentos.entradaDatos;

import java.util.Scanner;

public class UsoScanner {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("Ingrese su edad: ");
		
		int edad = input.nextInt();
		
		// Lee el espacio en blanco que quedó pendiente
		input.nextLine();
		
		System.out.print("Ingrese su nombre: ");
		
		String nombre = input.nextLine();
		
		System.out.println(String.format("Bienvenido %s. Tienes %d años", nombre, edad));
		
		input.close();
	}

}
