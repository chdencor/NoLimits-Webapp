from flask import Blueprint, render_template, request
from app.models.Cripto import Cripto

home_bp = Blueprint('home', __name__, template_folder='../views/templates')

@home_bp.route('/')
def index():
    return render_template('index.html')

@home_bp.route('/cripto')
def show_cripto():
    cripto_id = request.args.get('cripto_id')
    cripto = Cripto()
    data = cripto.get_cripto_data(cripto_id)
    return render_template('cripto.html', crypto=data)
