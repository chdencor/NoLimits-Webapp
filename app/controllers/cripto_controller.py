# app/controllers/crypto_controller.py
from flask import Blueprint, jsonify, request
from app.models.Cripto import Cripto

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
