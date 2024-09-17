from flask import Blueprint, jsonify, request, Response
from app.models.Cripto import Cripto
import matplotlib.pyplot as plt
import io

crypto_bp = Blueprint('crypto', __name__, template_folder='../views/templates')

@crypto_bp.route('/api/crypto/<string:cripto_id>', methods=['GET'])
def get_crypto_data(cripto_id):
    cripto = Cripto()
    data = {
        'symbol': cripto.getSymbol(cripto_id),
        'name': cripto.getName(cripto_id),
        'nameid': cripto.getNameid(cripto_id),
        'rank': cripto.getRank(cripto_id),
        'priceUsd': cripto.getPriceUsd(cripto_id),
        'percentChange24h': cripto.getPercentChange24h(cripto_id),
        'percentChange1h': cripto.getPercentChange1h(cripto_id),
        'percentChange7d': cripto.getPercentChange7d(cripto_id),
        'priceBtc': cripto.getPriceBtc(cripto_id),
        'marketCapUsd': cripto.getMarketCapUsd(cripto_id),
        'volume24': cripto.getVolume24(cripto_id),
        'volume24a': cripto.getVolume24a(cripto_id),
        'csupply': cripto.getCsupply(cripto_id),
        'tsupply': cripto.getTsupply(cripto_id),
        'msupply': cripto.getMsupply(cripto_id)
    }
    return jsonify(data)

@crypto_bp.route('/api/crypto/<string:cripto_id>/chart', methods=['GET'])
def get_crypto_chart(cripto_id):
    cripto = Cripto()

    # Simulación de datos para el ejemplo (puedes usar datos reales)
    changes = [
        cripto.getPercentChange1h(cripto_id),
        cripto.getPercentChange24h(cripto_id),
        cripto.getPercentChange7d(cripto_id)
    ]
    labels = ['1h', '24h', '7d']

    # Crear el gráfico
    plt.figure()
    plt.bar(labels, changes, color='blue')
    plt.xlabel('Periodo de tiempo')
    plt.ylabel('Cambio porcentual (%)')
    plt.title(f'Cambios porcentuales de {cripto.getSymbol(cripto_id)}')

    # Guardar gráfico en un buffer de memoria
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    # Devolver el gráfico como una imagen PNG
    return Response(buffer, mimetype='image/png')
