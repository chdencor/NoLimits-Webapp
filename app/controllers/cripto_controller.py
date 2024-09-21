from flask import Blueprint, jsonify, request, Response
from app.models.Cripto import Cripto
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import io

crypto_bp = Blueprint('crypto', __name__, template_folder='../views/templates')

@crypto_bp.route('/api/crypto/<string:cripto_id>', methods=['GET'])
def get_crypto_data(cripto_id):
    cripto = Cripto()
    data = {
        'symbol': cripto.getSymbol(cripto_id),
        'name': cripto.getName(cripto_id),
        'nameid': cripto.getNameId(cripto_id),
        'rank': cripto.getRank(cripto_id),
        'priceUsd': cripto.getPriceUsd(cripto_id),
        'percent_change_24h': cripto.getPercentChange24h(cripto_id),
        'percent_change_1h': cripto.getPercentChange1h(cripto_id),
        'percent_change_7d': cripto.getPercentChange7d(cripto_id),
        'price_btc': cripto.getPriceBtc(cripto_id),
        'market_cap_usd': cripto.getMarketCapUsd(cripto_id),
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
    changes = [
        cripto.getPercentChange1h(cripto_id),
        cripto.getPercentChange24h(cripto_id),
        cripto.getPercentChange7d(cripto_id)
    ]
    labels = ['1h', '24h', '7d']

    plt.figure()
    plt.bar(labels, changes, color='blue')
    plt.xlabel('Periodo de tiempo')
    plt.ylabel('Cambio porcentual (%)')
    plt.title(f'Cambios porcentuales de {cripto.getSymbol(cripto_id)}')

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)

    return Response(buffer, mimetype='image/png')