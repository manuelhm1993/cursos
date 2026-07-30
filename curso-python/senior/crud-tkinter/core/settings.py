import sys
from pathlib import Path

# 1. CONCIENCIA DE ENTORNO: ¿Soy un script o soy un .exe?
if getattr(sys, 'frozen', False):
    # --- MODO EJECUTABLE (PRODUCCIÓN) ---
    
    # Directorio donde vive el .exe (Perfecto para crear la BD y que el usuario la vea)
    EXEC_DIR = Path(sys.executable).parent
    
    # Directorio oculto temporal/interno de PyInstaller (Perfecto para leer el ícono)
    BUNDLE_DIR = Path(sys._MEIPASS)
else:
    # --- MODO SCRIPT (DESARROLLO EN VS CODE) ---
    EXEC_DIR = Path(__file__).resolve().parent.parent
    BUNDLE_DIR = EXEC_DIR

# 2. RESOLUCIÓN DE RUTAS SEPARADAS
ASSETS       = BUNDLE_DIR / "assets"           # Lee de la carpeta interna
DATA_DIR     = EXEC_DIR / "data"               # Escribe junto al .exe
DB_USUSARIOS = DATA_DIR / "usuarios.db"

# 3. AUTO-REPARACIÓN DE INFRAESTRUCTURA
# Creamos la carpeta de datos junto al .exe si no existe
DATA_DIR.mkdir(parents=True, exist_ok=True)