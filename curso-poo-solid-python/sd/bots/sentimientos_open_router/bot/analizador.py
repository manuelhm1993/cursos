from ..core.settings import OPENROUTER_API_KEY, BASE_URL, MODELO_IA, SYSTEM_INIT, ROLE
from openai import OpenAI 

class AnalizadorSentimientos:
    def __init__(self):
        # 1. Cargamos las variables de entorno de forma segura
        api_key = OPENROUTER_API_KEY

        # 2. Instanciamos el cliente de OpenAI apuntando a OpenRouter
        self._cliente = OpenAI(
            base_url=BASE_URL,
            api_key=api_key,
        )
        
        # OpenRouter recomienda usar modelos gratuitos para pruebas. "mistralai/mistral-7b-instruct:free"
        self._modelo = MODELO_IA

    @staticmethod
    def formatear_respuesta(respuesta: str) -> str:
        # Constante para resetear la consola al color original del usuario
        RESET = "\x1b[0m"

        colors_dict = {
            "negativo": "\x1b[1;31m", # Rojo
            "neutral": "\x1b[1;33m",  # Amarillo
            "positivo": "\x1b[1;32m"  # Verde
        }

        # 1. Usamos .get() por seguridad. Si la IA falla, usamos Blanco (37m) por defecto.
        default = "\x1b[1;37m"
        color   = colors_dict.get(respuesta, default)

        # 2. Inyectamos el color, la respuesta y CERRAMOS con RESET
        return f"{color}{respuesta.capitalize()}{RESET}"

    def analizar(self, texto_usuario: str) -> str:
        # Envía el texto a la IA y retorna el sentimiento detectado.
        try:
            # 3. Llamada a la API
            respuesta = self._cliente.chat.completions.create(
                model=self._modelo,
                messages=[
                    {
                        "role": ROLE[0],
                        "content": SYSTEM_INIT
                    },
                    {
                        "role": ROLE[1],
                        "content": texto_usuario
                    }
                ],
                # Temperature 0 hace que la respuesta sea determinista y precisa, ideal para análisis
                temperature=0.0, 
                max_tokens=8
            )
            
            # Extraemos el texto de la respuesta del objeto que devuelve OpenAI
            resultado = respuesta.choices[0].message.content.strip().lower()
            
            return AnalizadorSentimientos.formatear_respuesta(resultado)

        except Exception as e:
            # El comando "\x1b[1;31m" Pinta de rojo la consola 32 azul y así se combina
            return f"\x1b[1;31m[Error de Conexión]: {str(e)}\x1b[0m"