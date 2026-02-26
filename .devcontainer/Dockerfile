FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Instalamos Python y herramientas necesarias para los estudiantes
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y python3-pip python3-pymysql \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Instalamos librerías adicionales que pediste
RUN pip3 install --break-system-packages cryptography

