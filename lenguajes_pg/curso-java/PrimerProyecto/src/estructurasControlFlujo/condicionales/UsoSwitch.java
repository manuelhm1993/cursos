package estructurasControlFlujo.condicionales;

import java.util.Scanner;

public class UsoSwitch {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("Ingrese el número de mes deseado: ");
		
		int mes = input.nextInt();
		
		String respuesta = null;
		
		switch(mes) {
			case 1:
				respuesta = "Enero";
				break;
			case 2:
				respuesta = "Febrero";
				break;
			case 3:
				respuesta = "Marzo";
				break;
			case 4:
				respuesta = "Abril";
				break;
			case 5:
				respuesta = "Mayo";
				break;
			case 6:
				respuesta = "Junio";
				break;
			case 7:
				respuesta = "Julio";
				break;
			case 8:
				respuesta = "Agosto";
				break;
			case 9:
				respuesta = "Septiembre";
				break;
			case 10:
				respuesta = "Octubre";
				break;
			case 11:
				respuesta = "Noviembre";
				break;
			case 12:
				respuesta = "Diciembre";
				break;
			default:
				respuesta = "Mes no válido";
		}
		
		System.out.println(String.format("El número %d representa al mes %s", mes, respuesta));
		
		input.close();
	}

}
