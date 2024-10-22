from flask import Blueprint, render_template, request
from app.models.ORM import Criptomoneda, Registro
from app import db

home_bp = Blueprint('home', __name__, template_folder='../views/templates')

@home_bp.route('/')
def index():
    # Consultar las primeras 100 criptomonedas, ordenadas por el último registro rank
    top_cryptos = db.session.query(Criptomoneda).limit(100).all()

    # Preparar la lista de criptomonedas y sus últimos registros
    cryptos_with_latest_record = []
    for cripto in top_cryptos:
        latest_record = db.session.query(Registro).filter_by(criptomoneda_id=cripto.id).order_by(Registro.created_at.desc()).first()
        cryptos_with_latest_record.append((cripto, latest_record))

    # Ordenar las criptomonedas por el rank de su último registro
    cryptos_with_latest_record.sort(key=lambda x: (x[1].rank if x[1] else float('inf')))

    # Pasar los datos a la plantilla
    return render_template('index.html', cryptos=cryptos_with_latest_record)


@home_bp.route('/cripto')
def show_cripto():
    cripto_id = request.args.get('cripto_id')

    if cripto_id:
        # Consultar la criptomoneda por ID
        cripto = db.session.query(Criptomoneda).filter_by(id=cripto_id).first()

        if cripto:
            # Obtener el último registro de precios
            latest_record = db.session.query(Registro).filter_by(criptomoneda_id=cripto.id).order_by(Registro.created_at.desc()).first()
            return render_template('cripto.html', crypto=cripto, latest_record=latest_record)
        else:
            return render_template('error.html', message="Criptomoneda no encontrada"), 404
    else:
        return render_template('error.html', message="ID de criptomoneda no proporcionado"), 400
