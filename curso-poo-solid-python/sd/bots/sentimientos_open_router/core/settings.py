import os
from pathlib import Path
from dotenv import load_dotenv
from ..bot.formatear import Formatear

# 1. Calculamos la ruta base del proyecto (estilo el base_path() de Laravel)
# __file__ es este archivo (config/settigs.py) .parent es config/ .parent.parent es la raíz (sentimientos_open_router/)
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Le decimos a dotenv la ruta EXACTA de dónde está el .env
# Esto permite que el .env funcione sin importar desde dónde ejecutes el script
PATH_ENV = BASE_DIR / ".env"
load_dotenv(dotenv_path=PATH_ENV)

# 3. Extraemos las variables (Equivale a las llaves de tu array en Laravel)
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    # El comando "\x1b[1;31m" pinta de rojo la consola
    raise ValueError(f"{Formatear._ROJO}Error Crítico: No se encontró la KEY en la ruta: {PATH_ENV}{Formatear._RESET}")

# 4. Definimos el resto de configuraciones como constantes globales limpias
BASE_URL    = "https://openrouter.ai/api/v1"
MODELO_IA   = "deepseek/deepseek-chat"
ROLE        = ["system", "user", "assistant", "tool"]
SYSTEM_INIT = "Eres un analizador de sentimientos estricto. Analiza el texto del usuario y responde ÚNICAMENTE con una de estas tres palabras: 'Positivo', 'Negativo' o 'Neutral'. No agregues saludos, explicaciones ni puntos."