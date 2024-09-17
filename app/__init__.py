from flask import Flask
from app.controllers.cripto_controller import crypto_bp
from app.controllers.home_controller import home_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_bp)
    app.register_blueprint(crypto_bp)
    return app

