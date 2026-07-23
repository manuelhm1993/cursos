# 📦 Guía de Gestión de Paquetes Locales (Python)

Para crear, instalar y gestionar paquetes locales de forma profesional, sigue estos pasos:

### 1. Estructura del Paquete
Crea la carpeta de tu paquete con sus módulos y asegúrate de incluir los archivos `__init__.py` correspondientes para que Python lo reconoque formalmente.

### 2. Configuración (`setup.py`)
Crea el archivo `setup.py` en la raíz de tu proyecto. Asegúrate de definir correctamente el parámetro principal `name="nombre_de_tu_paquete"`.

### 3. Instalación
Para instalar el paquete dentro de tu entorno virtual (`.venv`), ubícate en la raíz del proyecto (donde está el `setup.py`) y ejecuta:

```bash
pip install .
```

> **💡 Tip de Desarrollo (Modo Editable):** > Si vas a estar modificando el código del paquete constantemente, instálalo con el flag `-e` (Editable). Esto crea un acceso directo simbólico (symlink) a tu código fuente, permitiendo que cualquier cambio que hagas en tus archivos `.py` se refleje inmediatamente en el entorno sin tener que volver a ejecutar la instalación:
> ```bash
> pip install -e .
> ```

### 4. Desinstalación
Para eliminar el paquete de tu entorno virtual, utiliza el comando `uninstall` seguido del **nombre registrado en el `setup.py`** (⚠️ *Importante: Es el nombre configurado en el archivo, no necesariamente el nombre de la carpeta física*).

```bash
pip uninstall nombre_de_tu_paquete
```

> **⚡ Pro-Tip de Limpieza:** Agrega el flag `-y` al final del comando para omitir el mensaje de confirmación (`[Y/n]`) y desinstalarlo de forma rápida y silenciosa:
> ```bash
> pip uninstall nombre_de_tu_paquete -y
> ```

### 5. Distribución manual
Se debe instalar en caso de que no exista el módulo build: `pip install build` y luego hacer la distribución `python -m build`