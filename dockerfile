# Usamos una imagen ligera de Python
FROM python:3.9-slim

# Definimos dónde vivirá el código dentro del contenedor
WORKDIR /app

# Copiamos los archivos de nuestra PC al contenedor
COPY . .
# requirements.txt . (cuando es un solo archivo)
# Instalamos las librerías
RUN pip install -r requirements.txt

# Exponemos el puerto 5000
EXPOSE 5000

# Comando para arrancar la app
CMD ["python", "app.py"]