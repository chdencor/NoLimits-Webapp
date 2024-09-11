# app/controllers/crypto_controller.py
from flask import Blueprint, jsonify, request
from app.models.Cripto import Cripto

crypto_bp = Blueprint('crypto', __name__, template_folder='../views/templates')

@crypto_bp.route('/api/crypto/<string:cripto_id>', methods=['GET'])
def get_crypto_data(cripto_id):
    cripto = Cripto()
    data = {
        'symbol': cripto.get_symbol(cripto_id),
        'name': cripto.get_name(cripto_id),
        'nameid': cripto.get_nameid(cripto_id),
        'rank': cripto.get_rank(cripto_id),
        'price_usd': cripto.get_price_usd(cripto_id),
        'percent_change_24h': cripto.get_percent_change_24h(cripto_id),
        'percent_change_1h': cripto.get_percent_change_1h(cripto_id),
        'percent_change_7d': cripto.get_percent_change_7d(cripto_id),
        'price_btc': cripto.get_price_btc(cripto_id),
        'market_cap_usd': cripto.get_market_cap_usd(cripto_id),
        'volume24': cripto.get_volume24(cripto_id),
        'volume24a': cripto.get_volume24a(cripto_id),
        'csupply': cripto.get_csupply(cripto_id),
        'tsupply': cripto.get_tsupply(cripto_id),
        'msupply': cripto.get_msupply(cripto_id)
    }
    return jsonify(data)
