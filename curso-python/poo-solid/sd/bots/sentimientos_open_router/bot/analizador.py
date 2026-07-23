from ..core.settings import OPENROUTER_API_KEY, BASE_URL, MODELO_IA, SYSTEM_INIT, ROLE
from .formatear import Formatear
from openai import OpenAI 

class Sentimientos(Formatear):
    __COLOR_DICT = {
        "negativo": Formatear._ROJO,
        "neutral":  Formatear._AMARILLO,
        "positivo": Formatear._VERDE
    }

    @staticmethod
    def formatear_texto(texto: str) -> str:
        # 1. Usamos .get() por seguridad. Si la IA falla, usamos Blanco (37m) por defecto.
        color = Sentimientos.__COLOR_DICT.get(texto, Sentimientos.__DEFAULT)

        # 2. Inyectamos el color, la respuesta y CERRAMOS con RESET
        return f"{color}{texto.capitalize()}{Sentimientos.__RESET}"

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
            
            return Sentimientos.formatear_texto(resultado)

        except Exception as e:
            return f"{Formatear._ROJO}[Error de Conexión]: {str(e)}{Formatear._RESET}"