FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que corre tu aplicación (ajusta según tu app)
EXPOSE 5000

# Comando para ejecutar tu aplicación usando Flask
CMD ["flask", "run", "--host=0.0.0.0"]
