# app/__init__.py
from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .controllers.home_controller import home_bp
    from .controllers.cripto_controller import crypto_bp
    
    app.register_blueprint(home_bp)
    app.register_blueprint(crypto_bp, url_prefix='/api')  # Prefix all API routes with /api
    
    return app

