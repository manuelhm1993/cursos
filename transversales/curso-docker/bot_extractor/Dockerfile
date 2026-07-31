# 1. Imagen base oficial de Python (versión ligera)
FROM python:3.12-slim

# 2. Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copiar SOLO las dependencias primero (Estrategia de Caché)
COPY requirements.txt .

# 4. Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copiar el resto del código de la aplicación
COPY . .

# 6. Comando de ignición del contenedor
CMD ["python", "main.py"]