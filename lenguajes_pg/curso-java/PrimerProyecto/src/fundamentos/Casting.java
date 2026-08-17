package fundamentos;

public class Casting {

	public static void main(String[] args) {
		byte numero1 = 15, numero2 = 25; // Declaración e inicialización múltiple
		
		/**
		 * En la suma de tipos primitivos se hace una conversión implícita a int o double para 
		 * optimización del procesador, la conversión explícita o casting se hace de la siguiente forma.
		 * El concepto se conoce como promoción de tipos
		 */
		byte resultado = (byte)(numero1 + numero2);
		
		// Variables declaradas como byte
		System.out.println("Tipo de numero1: " + ((Object)numero1).getClass().getSimpleName());
		System.out.println("Tipo de numero2: " + ((Object)numero2).getClass().getSimpleName());
		
		// Conversión implícita a int por parte del compilador
		System.out.println("Conversión implícita: " + ((Object)(numero1 + numero2)).getClass().getSimpleName());
		
		// Variable resultado como tipo byte después de una conversión explícita o casting
		System.out.println("Conversión explícita: " + ((Object)resultado).getClass().getSimpleName());
	}

}
