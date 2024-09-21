from flask import Blueprint, render_template, request
from app.models.Cripto import Cripto

home_bp = Blueprint('home', __name__, template_folder='../views/templates')
@home_bp.route('/')
def index():
    cripto = Cripto()
    data = cripto.parseResponse()  # Obtiene todas las criptomonedas
    top_cryptos = sorted(data, key=lambda x: x['rank'])[:100]  # Solo las top 100
    return render_template('index.html', cryptos=top_cryptos)

@home_bp.route('/cripto')
def show_cripto():
    cripto_id = request.args.get('cripto_id')
    if cripto_id:
        cripto = Cripto()
        data = cripto.getCriptoData(cripto_id)
        if data:
            return render_template('cripto.html', crypto=data)
        else:
            return render_template('error.html', message="Criptomoneda no encontrada"), 404
    else:
        return render_template('error.html', message="ID de criptomoneda no proporcionado"), 400
