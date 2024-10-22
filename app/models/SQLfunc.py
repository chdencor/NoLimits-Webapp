from sqlalchemy.orm import sessionmaker
from app.models.ORM import Criptomoneda

def get_cripto_param_by_symbol(session, symbol, param):
    """
    Recupera un parámetro específico de la criptomoneda con el símbolo dado.
    
    :param session: La sesión de SQLAlchemy.
    :param symbol: El símbolo de la criptomoneda.
    :param param: El nombre del parámetro que se desea recuperar.
    :return: El valor del parámetro solicitado o None si no existe.
    """
    allowed_params = [
        'id', 'name', 'symbol', 'msupply', 'price_usd', 'percent_change_24h',
        'percent_change_1h', 'percent_change_7d', 'price_btc', 'market_cap_usd',
        'volume24', 'volume24a', 'csupply', 'tsupply', 'created_at', 'rank'
    ]
    
    if param not in allowed_params:
        raise ValueError(f"Parámetro no válido: {param}. Parámetros permitidos: {allowed_params}")
    
    # Usar ORM para filtrar criptomoneda por símbolo
    cripto = session.query(Criptomoneda).filter_by(symbol=symbol).first()
    
    if cripto:
        # Devolver el valor del atributo solicitado
        return getattr(cripto, param, None)
    return None
