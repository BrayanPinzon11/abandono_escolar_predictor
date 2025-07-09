# Usa una imagen oficial de Python ligera
FROM python:3.11-slim

# Establece el directorio de trabajo
WORKDIR /app

# Copia solo los archivos necesarios primero
COPY requirements.txt .

# Instala dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el proyecto
COPY . .

# Expone el puerto para App Runner
EXPOSE 8080

# Comando de ejecución
CMD ["python", "app.py"]
