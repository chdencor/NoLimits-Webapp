import time
from app.models.Cripto import Cripto
from app.models.supabaseDAO import SupabaseDAO
from app.config import Config

# Configura tu conexión a Supabase
dao_instance = SupabaseDAO(Config.SUPABASE_DB_URL)

def data_loader():
    """
    Función que se ejecutará en segundo plano para obtener datos de criptomonedas
    y almacenarlos periódicamente en la base de datos.
    """
    cripto = Cripto()

    while True:
        # Obtener datos de la API
        data = cripto.parseResponse()

        for item in data:
            # Verificar si la criptomoneda ya existe en la tabla 'criptomonedas'
            existing_cripto = dao_instance.fetch_one('criptomonedas', item['symbol'])

            if not existing_cripto:
                # Insertar nueva criptomoneda si no existe
                cripto_columns = ['symbol', 'name']
                cripto_values = [item['symbol'], item['name']]
                cripto_id = dao_instance.create('criptomonedas', cripto_columns, cripto_values)
            else:
                cripto_id = existing_cripto[0]  # Supongamos que el ID está en la primera columna

            # Insertar el nuevo registro en la tabla 'registros'
            registro_columns = ['price_usd', 'percent_change_24h', 'percent_change_1h', 
                                'percent_change_7d', 'price_btc', 'market_cap_usd', 
                                'volume24', 'volume24a', 'csupply', 'tsupply', 'msupply']
            registro_values = [item['price_usd'], item['percent_change_24h'], item['percent_change_1h'],
                               item['percent_change_7d'], item['price_btc'], item['market_cap_usd'],
                               item['volume24'], item['volume24a'], item['csupply'], item['tsupply'], item['msupply']]
            registro_id = dao_instance.create('registros', registro_columns, registro_values)

            # Insertar el vínculo en la tabla intermedia 'registros_por_criptomoneda'
            intermedia_columns = ['criptomoneda_id', 'registro_id']
            intermedia_values = [cripto_id, registro_id]
            dao_instance.create('registros_por_criptomoneda', intermedia_columns, intermedia_values)

        # Esperar 30 segundos antes de la próxima ejecución
        time.sleep(30)

