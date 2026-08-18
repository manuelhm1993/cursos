package estructurasControlFlujo.condicionales;

import java.util.Scanner;

public class SwitchV14Plus {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("Ingrese el número de mes deseado: ");
		
		int mes = input.nextInt();
		
		// Es exáctamente lo mismo que match en php 8+, permite usar el switch como expresión
		String respuesta = switch(mes) {
			case 1 	-> "Enero";
			case 2 	-> "Febrero";
			case 3 	-> "Marzo";
			case 4 	-> "Abril";
			case 5 	-> "Mayo";
			case 6 	-> "Junio";
			case 7 	-> "Julio";
			case 8 	-> "Agosto";
			case 9 	-> "Septiembre";
			case 10 -> "Octubre";
			case 11 -> "Noviembre";
			case 12 -> "Diciembre";
			default -> "Mes no válido";
		};
		
		System.out.println(String.format("El número %d representa al mes %s", mes, respuesta));
		
		input.close();
	}

}
