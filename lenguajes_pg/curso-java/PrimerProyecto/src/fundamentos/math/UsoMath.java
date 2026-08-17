package fundamentos.math;

import java.math.BigInteger;

public class UsoMath {

	public static void main(String[] args) {
		valorMaximo(7, 3);
	}
	
	public static void valorMaximo(int num1, int num2) {
		int maximo = Math.max(num1, num2);
		
		System.out.println("Valor máximo: " + maximo);
	}
	
	public static void valorAbsoluto(int numero) {
		int absoluto = Math.abs(numero);
		
		System.out.println(absoluto);
	}
	
	public static void numeroAleatorio() {
		int aleatorio = Math.round((float)(Math.random() * 100));
		
		System.out.println(aleatorio);
	}
	
	public static void potenciaBigInteger(int base, int exponente) {
		BigInteger b = BigInteger.valueOf(base);
		
		BigInteger potencia = b.pow(exponente);
		
		System.out.println(base + " ^ " + exponente + " = " + potencia);
	}
	
	public static void sacarPotencia(double base, double exponente) {
		double potencia = Math.pow(base, exponente);
		
		System.out.println(base + " ^ " + exponente + " = " + potencia);
	}
	
	public static void conversiones(int numero) {
		// Conversión explícita e implícita
		int raiz = (int)Math.sqrt(numero);
		
		System.out.println("La raíz de " + numero + " es: " + raiz);
	}
}
