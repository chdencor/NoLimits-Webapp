import time
from app.models.Cripto import Cripto
from app.models.supabaseDAO import SupabaseDAO
from app.config import Config
from app.models.RegistroCrudo import Registro

# Configura tu conexión a Supabase
dao_instance = SupabaseDAO(Config.DATABASE_URL)

def dataLoader():
    cripto = Cripto()
    registro = Registro()  # Instancia de Registro para manejar el archivo JSON

    while True:
        # Obtener datos de la API
        data = cripto.parseResponse()
        ids_obtenidos = []  # Para almacenar los IDs obtenidos

        for item in data:
            # Agregar el ID actual a la lista
            ids_obtenidos.append(item['id'])

            # Verificar si la criptomoneda ya existe en la base de datos
            existing_cripto = dao_instance.fetchOne('criptomonedas', item['id'])
            if existing_cripto:
                print(f"ID {item['id']} ya existe en la base de datos, se omite la inserción.")
                cripto_id = existing_cripto['id']  # Usar el ID existente para el registro
            else:
                # Insertar nueva criptomoneda si no existe en la base de datos
                cripto_columns = ['name', 'symbol']
                cripto_values = [item['name'], item['symbol']]
                cripto_id = dao_instance.createCripto('criptomonedas', cripto_columns, cripto_values)

                if cripto_id is None:
                    print(f"La criptomoneda {item['name']} ya existe, se omite la inserción.")
                    continue
                print(f"Nueva criptomoneda insertada con ID: {cripto_id}")

            # Definir columnas para el registro
            registro_columns = ['price_usd', 'percent_change_24h', 'percent_change_1h', 
                                'percent_change_7d', 'price_btc', 'market_cap_usd', 
                                'volume24', 'volume24a', 'csupply', 'tsupply', 'msupply']
            registro_values = [
                item.get('price_usd', None),
                item.get('percent_change_24h', None),
                item.get('percent_change_1h', None),
                item.get('percent_change_7d', None),
                item.get('price_btc', None),
                item.get('market_cap_usd', None),
                item.get('volume24', None),
                item.get('volume24a', None),
                item.get('csupply', None),
                item.get('tsupply', None),
                item.get('msupply', None)
            ]

            # Filtrar valores vacíos o no válidos
            if any(value is None or (isinstance(value, str) and value.strip() == "") for value in registro_values):
                print("Error: Hay valores vacíos en los datos del registro, se omite la inserción.")
                continue

            try:
                registro_id = dao_instance.create('registros', registro_columns, registro_values)
                print(f"Nuevo registro insertado con ID: {registro_id}")

                # Insertar el vínculo en la tabla intermedia 'registros_por_criptomoneda'
                intermedia_columns = ['criptomoneda_id', 'registro_id']
                intermedia_values = [cripto_id, registro_id]
                dao_instance.create('registros_por_criptomoneda', intermedia_columns, intermedia_values)
                print("Vínculo insertado en registros_por_criptomoneda.")
                
                # Actualizar el registro en el archivo JSON
                registro.actualizarCripto(ids_obtenidos)
                print("Archivo JSON actualizado con nuevos IDs.")

            except Exception as e:
                print(f"Error al insertar registro: {e}")

        # Esperar 30 segundos antes de la próxima ejecución
        time.sleep(30)
