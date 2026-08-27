package estructurasControlFlujo.bucles.determinados;

public class UsoForEach {

	public static void main(String[] args) {
		String[] paises = {
			"Venezuela", "España", "Rusia", "Alemania",
			"Chile", "Colombia", "Francia", "USA",
			"México"
		};
		
		// Bucle foreach, por cada elemento del array se crea un objeto copia de solo lectura
		for(String pais: paises) {
			System.out.println(String.format("País: %s", pais));
		}
	}

}
