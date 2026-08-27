package fundamentos.arrays;

public class UsoArrays {

	public static void main(String[] args) {
		// Declarar e inicializar un array
		/*int[] edades = new int[5];
		
		// Darle valor a cada posición de un array
		edades[0] = 5;
		edades[1] = 15;
		edades[2] = 51;
		edades[3] = 53;
		edades[4] = 95;*/
		
		int[] edades = {
			5,15,51,53,95,
			76,54,98,34,90,
			67,54,98,32,1,
			0,98,97,105,1,
			2,7,71
		};
		
		int n_items = edades.length;
		
		// Ver los elementos de un array
		for(int i=0;i<n_items;i++) {
			System.out.println(String.format("Valor del índice %d = %d", i, edades[i]));
		}
	}

}
