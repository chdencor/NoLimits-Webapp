from flask import Blueprint, jsonify, request, Response
from app.models.ORM import Criptomoneda, Registro  # Importar Registro
import matplotlib.pyplot as plt
import matplotlib
import io
from app import db

matplotlib.use('Agg')

crypto_bp = Blueprint('crypto', __name__, template_folder='../views/templates')

@crypto_bp.route('/api/crypto/<int:cripto_id>', methods=['GET'])
def get_crypto_data(cripto_id):
    # Buscar la criptomoneda por ID
    cripto = db.session.query(Criptomoneda).filter_by(id=cripto_id).first()

    if not cripto:
        return jsonify({'error': 'Criptomoneda no encontrada'}), 404

    # Obtener el último registro de precios
    latest_record = db.session.query(Registro).filter_by(criptomoneda_id=cripto.id).order_by(Registro.created_at.desc()).first()

    # Crear el diccionario con los datos de la criptomoneda
    data = {
        'symbol': cripto.symbol,
        'name': cripto.name,
        'nameid': cripto.id,
        'rank': latest_record.rank if latest_record else None,
        'msupply': cripto.msupply,
        'priceUsd': latest_record.price_usd if latest_record else None,
        'percent_change_24h': latest_record.percent_change_24h if latest_record else None,
        'percent_change_1h': latest_record.percent_change_1h if latest_record else None,
        'percent_change_7d': latest_record.percent_change_7d if latest_record else None,
        'price_btc': latest_record.price_btc if latest_record else None,
        'market_cap_usd': latest_record.market_cap_usd if latest_record else None,
        'volume24': latest_record.volume24 if latest_record else None,
        'volume24a': latest_record.volume24a if latest_record else None,
        'csupply': latest_record.csupply if latest_record else None,
        'tsupply': latest_record.tsupply if latest_record else None,
        'latest_update': latest_record.latest_update.isoformat() if latest_record and latest_record.latest_update else None  # Agregar este campo
    }

    return jsonify(data)

@crypto_bp.route('/api/crypto/<int:cripto_id>/chart', methods=['GET'])
def get_crypto_chart(cripto_id):
    # Buscar la criptomoneda por ID
    cripto = db.session.query(Criptomoneda).filter_by(id=cripto_id).first()

    if not cripto:
        return jsonify({'error': 'Criptomoneda no encontrada'}), 404

    # Obtener todos los registros para la criptomoneda
    registros = db.session.query(Registro).filter_by(criptomoneda_id=cripto.id).all()

    if not registros:
        return jsonify({'error': 'No se encontraron registros para esta criptomoneda'}), 404

    # Recoger los cambios porcentuales
    changes = [
        registros[-1].percent_change_1h,  # Último registro
        registros[-1].percent_change_24h,
        registros[-1].percent_change_7d
    ]
    labels = ['1h', '24h', '7d']

    plt.figure()
    plt.bar(labels, changes, color='blue')
    plt.xlabel('Periodo de tiempo')
    plt.ylabel('Cambio porcentual (%)')
    plt.title(f'Cambios porcentuales de {cripto.symbol}')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    return Response(buffer.getvalue(), mimetype='image/png')
