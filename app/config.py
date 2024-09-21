import os
class Config:
    SECRET_KEY = 'mi_clave_secreta'

    # Configuración de la base de datos
    DATABASE_URL = os.getenv("DATABASE_URL")