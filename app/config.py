import os
class Config:

    # Configuración de la base de datos
    DATABASE_URL = os.getenv("DATABASE_URL")