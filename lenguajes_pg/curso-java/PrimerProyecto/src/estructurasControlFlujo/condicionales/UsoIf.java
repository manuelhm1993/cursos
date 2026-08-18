package estructurasControlFlujo.condicionales;

import java.util.Scanner;

public class UsoIf {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("Ingrese su edad: ");
		
		String edadIn = input.nextLine();
		
		// Mantener plano y evitar anidamientos
		if(!edadIn.matches("[0-9]+")) {
			System.out.println("Debes ingresar un número entero positivo");
			input.close();
			return;
		}
		
		int edad = Integer.parseInt(edadIn);
		
		if(edad > 0 && edad <= 110) {
			System.out.println((edad >= 18) ? "Eres mayor de edad" : "Eres menor de edad");
		}
		else {
			System.out.println("Edad incorrecta");
		}
		
		input.close();
	}

}
