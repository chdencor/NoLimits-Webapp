from flask import Blueprint, render_template
from app.models.user import User

home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index():
    # Ejemplo de uso de un modelo
    user = User.get_user()
    return render_template('index.html', user=user)
