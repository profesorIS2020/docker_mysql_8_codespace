FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Instalamos dependencias del sistema
# 1. Eliminamos docker.io (porque ya lo pusimos en las 'features' del devcontainer.json)
# 2. Añadimos el flag --no-install-recommends para que la imagen sea más ligera
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install -y --no-install-recommends \
    python3 \
    python3-pip \
    && apt-get clean -y && rm -rf /var/lib/apt/lists/*

# Instalamos librerías de Python
# Usamos --break-system-packages porque en Ubuntu 24.04 pip está bloqueado 
# a nivel de sistema para proteger el SO (PEP 668).
RUN pip3 install --break-system-packages pymysql cryptography

