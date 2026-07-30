from .bot.analizador import AnalizadorSentimientos

# --- Punto de Entrada del Programa ---
if __name__ == "__main__":
    print("--- Iniciando Chatbot Analizador de Sentimientos ---")
    
    try:
        # Instanciamos nuestra clase
        analizador = AnalizadorSentimientos()
        
        while True:
            # Bucle infinito para interactuar con el usuario
            entrada = input("\nEscribe una frase (o escribe 'salir' para terminar): ")
            
            if entrada.lower() in ['salir', 'exit', 'quit']:
                print("Cerrando el analizador. ¡Hasta pronto!")
                break
                
            if not entrada.strip():
                print("Por favor, escribe algo válido.")
                continue

            print("Analizando...")
            sentimiento = analizador.analizar(entrada)
            print(f">> Resultado: {sentimiento}")

    except ValueError as e:
        # Atrapa el error si falta el .env
        print(e)