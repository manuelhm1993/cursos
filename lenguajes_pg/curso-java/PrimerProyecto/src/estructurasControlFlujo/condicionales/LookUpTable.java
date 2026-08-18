package estructurasControlFlujo.condicionales;

import java.util.Map;
import java.util.Scanner;
import static java.util.Map.entry; // Importación estática obligatoria para usar entry() directamente

public class LookUpTable {

    public static void main(String[] args) {
        // 1. Construcción de la Lookup Table inmutable (>10 elementos)
        // Se define fuera de la lógica principal. Es pura data estática.
        Map<Integer, String> meses = Map.ofEntries(
            entry(1, "Enero"),
            entry(2, "Febrero"),
            entry(3, "Marzo"),
            entry(4, "Abril"),
            entry(5, "Mayo"),
            entry(6, "Junio"),
            entry(7, "Julio"),
            entry(8, "Agosto"),
            entry(9, "Septiembre"),
            entry(10, "Octubre"),
            entry(11, "Noviembre"),
            entry(12, "Diciembre")
        );

        Scanner input = new Scanner(System.in);
        
        System.out.print("Ingrese el número de mes deseado: ");
        int mes = input.nextInt();
        
        // 2. Extracción O(1) con manejo de error (Default) integrado
        String respuesta = meses.getOrDefault(mes, "Mes no válido");
        
        System.out.println(String.format("El número %d representa al mes %s", mes, respuesta));
        
        input.close();
    }
}