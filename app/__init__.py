from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Inicializar la instancia de SQLAlchemy
db = SQLAlchemy()

def create_app():
    # Cargar las variables de entorno desde el archivo .env
    load_dotenv('db_url.env')

    # Obtener la URL de la base de datos desde las variables de entorno
    database_url = os.getenv("DATABASE_URL")
    if not database_url:
        raise ValueError("DATABASE_URL no está definida en db_url.env")
    print("DATABASE_URL:", database_url)

    # Crear la aplicación Flask
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_url
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Inicializar la extensión de la base de datos con la aplicación
    db.init_app(app)

    # Registrar los controladores (blueprints)
    from app.controllers.home_controller import home_bp
    from app.controllers.cripto_controller import crypto_bp
    
    app.register_blueprint(home_bp)
    app.register_blueprint(crypto_bp)

    return app
