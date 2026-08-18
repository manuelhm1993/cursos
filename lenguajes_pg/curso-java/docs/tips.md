```java
// String Template en Java 21 (Preview)
String nombre = "Manuel";
int edad = 30;
String mensaje = STR."Mi nombre es \{nombre} y tengo \{edad} años.";

// Lookup table
import java.util.Map;

public class Main {
    public static void main(String[] args) {
        // 1. Definimos la Lookup Table inmutable
        Map<String, String> dias = Map.of(
            "L", "Laboral",
            "S", "Fin de Semana"
            // Nota: Map.of soporta hasta 10 pares clave-valor directos.
        );

        String input = "L";
        
        // 2. Extracción segura con Default (Equivalente al .get(key, default) de Python)
        String resultado = dias.getOrDefault(input, "Día no registrado");
        
        System.out.println(resultado);
    }
}
```