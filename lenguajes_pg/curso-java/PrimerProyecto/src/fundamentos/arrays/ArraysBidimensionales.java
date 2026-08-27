package fundamentos.arrays;

public class ArraysBidimensionales {

	public static void main(String[] args) {
		int[][] numeros = {
			{15, 21, 18, 9, 15}, 
			{10, 52, 17, 19, 7}, 
			{19, 2, 19, 17, 7},
			{92, 13, 29, 45, 69}
		};
		
		for(int[] i: numeros) {
			for(int j: i) {
				System.out.print(j + " ");
			}
			System.out.print("\n");
		}
	}

}
