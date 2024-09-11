from flask import Flask

def create_app():
    app = Flask(__name__)
    
    # Configuraciones opcionales
    # app.config.from_object('app.config.Config')

    # Importar y registrar controladores
    from .controllers.home_controller import home_bp
    app.register_blueprint(home_bp)

    return app
