# Usamos una imagen base ligera de Python
FROM python:3.11-slim

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el archivo de requerimientos y lo instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos la aplicación en el contenedor
COPY app /app/app

# Exponemos el puerto
EXPOSE 5000

# Ejecutamos la aplicación
CMD ["python", "app/main.py"]
