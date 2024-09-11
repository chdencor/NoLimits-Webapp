"""
Clase Cripto que contiene todos los metodos
para recuperar la informacion de las criptomonedas.
"""

from APICripto import APICripto

class Cripto:
    """
    Clase Cripto que contiene todos los métodos para recuperar la información de las criptomonedas.
    """

    def __init__(self):
        self.data = APICripto()
        self.respuesta = self.data.APICall(self.data.url)  # Llamada a la API

    def parse_response(self):
        """
        Convierte la respuesta de la API a JSON y la parsea para obtener los datos.

        :return: Lista de diccionarios con los datos de las criptomonedas.
        :rtype: list
        """
        parsed_response = self.data.APIParsing(self.respuesta)
        dataRetrieved = self.data.getKeyValue(parsed_response)
        return dataRetrieved

    def get_cripto_data(self, cripto_id):
        """
        Obtiene los datos de una criptomoneda específica por su ID.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: Diccionario con los datos de la criptomoneda.
        :rtype: dict
        """
        dataRetrieved = self.parse_response()
        for item in dataRetrieved:
            if item.get("id") == cripto_id:
                return item
        return None
    
    def getAllids(self):
        globalData = self.parse_response()
        idList = [item.get('id') for item in globalData if item.get('id') is not None]
    
        return idList



    def get_symbol(self, cripto_id):
        """
        Obtiene el símbolo de una criptomoneda específica.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: Símbolo de la criptomoneda.
        :rtype: str
        """
        cripto_data = self.get_cripto_data(cripto_id)
        return cripto_data.get("symbol") if cripto_data else None

    def get_name(self, cripto_id):
        """
        Obtiene el nombre de una criptomoneda específica.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: Nombre de la criptomoneda.
        :rtype: str
        """
        cripto_data = self.get_cripto_data(cripto_id)
        return cripto_data.get("name") if cripto_data else None

    def get_nameid(self, cripto_id):
        """
        Obtiene el 'nameid' de una criptomoneda específica.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: 'Nameid' de la criptomoneda.
        :rtype: str
        """
        cripto_data = self.get_cripto_data(cripto_id)
        return cripto_data.get("nameid") if cripto_data else None

    def get_rank(self, cripto_id):
        """
        Obtiene el ranking de una criptomoneda específica.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: Ranking de la criptomoneda.
        :rtype: int
        """
        cripto_data = self.get_cripto_data(cripto_id)
        return cripto_data.get("rank") if cripto_data else None

    def get_price_usd(self, cripto_id):
        """
        Obtiene el precio en USD de una criptomoneda específica.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: Precio en USD de la criptomoneda.
        :rtype: str
        """
        cripto_data = self.get_cripto_data(cripto_id)
        return cripto_data.get("price_usd") if cripto_data else None

    def get_percent_change_24h(self, cripto_id):
        """
        Obtiene el porcentaje de cambio en las últimas 24 horas de una criptomoneda específica.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: Porcentaje de cambio en las últimas 24 horas.
        :rtype: str
        """
        cripto_data = self.get_cripto_data(cripto_id)
        return cripto_data.get("percent_change_24h") if cripto_data else None

    def get_percent_change_1h(self, cripto_id):
        """
        Obtiene el porcentaje de cambio en la última hora de una criptomoneda específica.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: Porcentaje de cambio en la última hora.
        :rtype: str
        """
        cripto_data = self.get_cripto_data(cripto_id)
        return cripto_data.get("percent_change_1h") if cripto_data else None

    def get_percent_change_7d(self, cripto_id):
        """
        Obtiene el porcentaje de cambio en los últimos 7 días de una criptomoneda específica.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: Porcentaje de cambio en los últimos 7 días.
        :rtype: str
        """
        cripto_data = self.get_cripto_data(cripto_id)
        return cripto_data.get("percent_change_7d") if cripto_data else None

    def get_price_btc(self, cripto_id):
        """
        Obtiene el precio en BTC de una criptomoneda específica.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: Precio en BTC de la criptomoneda.
        :rtype: str
        """
        cripto_data = self.get_cripto_data(cripto_id)
        return cripto_data.get("price_btc") if cripto_data else None

    def get_market_cap_usd(self, cripto_id):
        """
        Obtiene la capitalización de mercado en USD de una criptomoneda específica.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: Capitalización de mercado en USD de la criptomoneda.
        :rtype: str
        """
        cripto_data = self.get_cripto_data(cripto_id)
        return cripto_data.get("market_cap_usd") if cripto_data else None

    def get_volume24(self, cripto_id):
        """
        Obtiene el volumen en las últimas 24 horas de una criptomoneda específica.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: Volumen en las últimas 24 horas.
        :rtype: float
        """
        cripto_data = self.get_cripto_data(cripto_id)
        return cripto_data.get("volume24") if cripto_data else None

    def get_volume24a(self, cripto_id):
        """
        Obtiene el volumen ajustado en las últimas 24 horas de una criptomoneda específica.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: Volumen ajustado en las últimas 24 horas.
        :rtype: float
        """
        cripto_data = self.get_cripto_data(cripto_id)
        return cripto_data.get("volume24a") if cripto_data else None

    def get_csupply(self, cripto_id):
        """
        Obtiene la oferta circulante de una criptomoneda específica.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: Oferta circulante.
        :rtype: str
        """
        cripto_data = self.get_cripto_data(cripto_id)
        return cripto_data.get("csupply") if cripto_data else None

    def get_tsupply(self, cripto_id):
        """
        Obtiene la oferta total de una criptomoneda específica.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: Oferta total.
        :rtype: str
        """
        cripto_data = self.get_cripto_data(cripto_id)
        return cripto_data.get("tsupply") if cripto_data else None

    def get_msupply(self, cripto_id):
        """
        Obtiene la oferta máxima de una criptomoneda específica.

        :param cripto_id: ID de la criptomoneda.
        :type cripto_id: str
        :return: Oferta máxima.
        :rtype: str
        """
        cripto_data = self.get_cripto_data(cripto_id)
        return cripto_data.get("msupply") if cripto_data else None

