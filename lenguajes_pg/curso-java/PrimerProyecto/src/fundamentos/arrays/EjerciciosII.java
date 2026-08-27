package fundamentos.arrays;

import java.text.NumberFormat;
import java.util.Locale;

public class EjerciciosII {

	public static void main(String[] args) {
		double[][] inversiones = new double[5][6];
		double intereses = 0.10;
		
		int itemsI = inversiones.length, itemsJ = inversiones[0].length;
		
		for(int i=0; i<itemsI; i++) {
			for(int j=0; j<itemsJ; j++) {
				if(i == 0) {
					inversiones[i][j] = 10000.0;
				}
				else {
					inversiones[i][j] = inversiones[i-1][j] + (inversiones[i-1][j] * intereses);
					intereses += 0.01;
				}
			}
			intereses = 0.10;
		}
		
		Locale es = Locale.of("es", "ES");
		NumberFormat formatoES = NumberFormat.getCurrencyInstance(es);
		
		for(double[] i: inversiones) {
			for(double j: i) {
				// System.out.print(String.format("%.2f € ", j));
				System.out.print(formatoES.format(j) + " ");
			}
			System.out.println();
		}
	}

}
