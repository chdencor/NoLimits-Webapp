from flask import Flask
from app.controllers.cripto_controller import crypto_bp
from app.controllers.home_controller import home_bp
from threading import Thread
from app.models.data_loader import data_loader  # Importamos el hilo del data_loader
from app.models.supabaseDAO import SupabaseDAO
from app.config import Config

def create_app():
    app = Flask(__name__)
    
    # Registrar Blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(crypto_bp)
    
    # Configura tu conexión a Supabase
    dao_instance = SupabaseDAO(Config.SUPABASE_DB_URL)
    dao_instance.connect()

    # Iniciar el hilo de carga de datos
    loader_thread = Thread(target=data_loader)
    loader_thread.daemon = True  # El hilo se cerrará cuando se cierre la aplicación principal
    loader_thread.start()

    return app
