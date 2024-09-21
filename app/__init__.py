from flask import Flask
from app.controllers.cripto_controller import crypto_bp
from app.controllers.home_controller import home_bp
from threading import Thread
from app.models.data_loader import dataLoader
from app.models.supabaseDAO import SupabaseDAO
from app.config import Config
from dotenv import load_dotenv
import os

def create_app():

    # Cargar variables de entorno desde el archivo .env
    load_dotenv('db_url.env')

    # Verificar si DATABASE_URL está correctamente cargada
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL no está definida en db_url.env")
    print("DATABASE_URL:", database_url)

    app = Flask(__name__)

    # Registrar Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(crypto_bp)
    
    # Conexión a la base de datos
    dao_instance = SupabaseDAO(database_url)  # Usar la variable de entorno
    dao_instance.connect()

    # Iniciar el hilo para el data_loader
    loader_thread = Thread(target=dataLoader)
    loader_thread.daemon = True  # El hilo se cerrará cuando se cierre la aplicación
    loader_thread.start()

    return app
