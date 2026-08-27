package estructurasControlFlujo.condicionales;

import java.util.Scanner;

public class OperadorTernario {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("Ingrese su edad: ");
		
		String edadIn = input.nextLine();
		
		// Condicionales anidados
		if(edadIn.matches("[0-9]+")) {
			int edad = Integer.parseInt(edadIn);
			
			if(edad > 0 && edad <= 110) {
				// Operador ternario
				System.out.println((edad >= 18) ? "Eres mayor de edad" : "Eres menor de edad");
			}
			else {
				System.out.println("Edad incorrecta");
			}
		}
		else {
			System.out.println("Debes ingresar un número entero positivo");
		}
		
		input.close();
	}

}
