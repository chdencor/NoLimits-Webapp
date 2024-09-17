from flask import Blueprint, render_template, request
from app.models.Cripto import Cripto

home_bp = Blueprint('home', __name__, template_folder='../views/templates')

@home_bp.route('/')
def index():
    return render_template('index.html')

@home_bp.route('/cripto')
def show_cripto():
    cripto_id = request.args.get('cripto_id')
    if cripto_id:
        cripto = Cripto()
        data = cripto.getCriptoData(cripto_id)
        if data:
            return render_template('cripto.html', crypto=data)
        else:
            # Manejar el caso en que no se encontró la criptomoneda
            return render_template('error.html', message="Criptomoneda no encontrada"), 404
    else:
        # Manejar el caso en que no se proporcionó el ID
        return render_template('error.html', message="ID de criptomoneda no proporcionado"), 400
