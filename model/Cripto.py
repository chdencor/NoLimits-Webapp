"""
Clase Cripto que contiene todos los metodos
para recuperar la informacion de las criptomonedas.
"""

from APICripto import APICripto

class Cripto:
    def _init_(self):
        self.data = APICripto()
        self.respuesta = self.data.APICall(self.data.url)  # Llamada a la API

    def parse_response(self):
        # Convierte la respuesta de la API a JSON y la parsea para obtener los datos
        parsed_response = self.data.APIParsing(self.respuesta)
        dataRetrieved = self.data.getKeyValue(parsed_response)
        return dataRetrieved

    def get_Ids(self):
        # Obtiene todos los IDs de las criptomonedas
        dataRetrieved = self.parse_response()
        ids = [item.get("id") for item in dataRetrieved]
        return ids

    def get_symbols(self):
        # Obtiene todos los símbolos de las criptomonedas
        dataRetrieved = self.parse_response()
        symbols = [item.get("symbol") for item in dataRetrieved]
        return symbols

    def get_names(self):
        # Obtiene todos los nombres de las criptomonedas
        dataRetrieved = self.parse_response()
        names = [item.get("name") for item in dataRetrieved]
        return names

    def get_nameids(self):
        # Obtiene todos los 'nameid' de las criptomonedas
        dataRetrieved = self.parse_response()
        nameids = [item.get("nameid") for item in dataRetrieved]
        return nameids

    def get_rank(self):
        # Obtiene el ranking de todas las criptomonedas
        dataRetrieved = self.parse_response()
        ranks = [item.get("rank") for item in dataRetrieved]
        return ranks

    def get_price_usd(self):
        # Obtiene el precio en USD de todas las criptomonedas
        dataRetrieved = self.parse_response()
        prices_usd = [item.get("price_usd") for item in dataRetrieved]
        return prices_usd

    def get_percent_change_24h(self):
        # Obtiene el porcentaje de cambio en las últimas 24 horas de todas las criptomonedas
        dataRetrieved = self.parse_response()
        percent_change_24h = [item.get("percent_change_24h") for item in dataRetrieved]
        return percent_change_24h

    def get_percent_change_1h(self):
        # Obtiene el porcentaje de cambio en la última hora de todas las criptomonedas
        dataRetrieved = self.parse_response()
        percent_change_1h = [item.get("percent_change_1h") for item in dataRetrieved]
        return percent_change_1h

    def get_percent_change_7d(self):
        # Obtiene el porcentaje de cambio en los últimos 7 días de todas las criptomonedas
        dataRetrieved = self.parse_response()
        percent_change_7d = [item.get("percent_change_7d") for item in dataRetrieved]
        return percent_change_7d

    def get_price_btc(self):
        # Obtiene el precio en BTC de todas las criptomonedas
        dataRetrieved = self.parse_response()
        prices_btc = [item.get("price_btc") for item in dataRetrieved]
        return prices_btc

    def get_market_cap_usd(self):
        # Obtiene la capitalización de mercado en USD de todas las criptomonedas
        dataRetrieved = self.parse_response()
        market_cap_usd = [item.get("market_cap_usd") for item in dataRetrieved]
        return market_cap_usd

    def get_volume24(self):
        # Obtiene el volumen en las últimas 24 horas de todas las criptomonedas
        dataRetrieved = self.parse_response()
        volume24 = [item.get("volume24") for item in dataRetrieved]
        return volume24

    def get_volume24a(self):
        # Obtiene el volumen ajustado en las últimas 24 horas de todas las criptomonedas
        dataRetrieved = self.parse_response()
        volume24a = [item.get("volume24a") for item in dataRetrieved]
        return volume24a

    def get_csupply(self):
        # Obtiene la oferta circulante de todas las criptomonedas
        dataRetrieved = self.parse_response()
        csupply = [item.get("csupply") for item in dataRetrieved]
        return csupply

    def get_tsupply(self):
        # Obtiene la oferta total de todas las criptomonedas
        dataRetrieved = self.parse_response()
        tsupply = [item.get("tsupply") for item in dataRetrieved]
        return tsupply

    def get_msupply(self):
        # Obtiene la oferta máxima de todas las criptomonedas
        dataRetrieved = self.parse_response()
        msupply = [item.get("msupply") for item in dataRetrieved]
        return msupply


def main():
    cripto = Cripto()

    # Mostrar los resultados de cada getter
    print("IDs:", cripto.get_Ids())
    print("Símbolos:", cripto.get_symbols())
    print("Nombres:", cripto.get_names())
    print("Name IDs:", cripto.get_nameids())
    print("Rankings:", cripto.get_rank())
    print("Precios en USD:", cripto.get_price_usd())
    print("Cambio % en 24h:", cripto.get_percent_change_24h())
    print("Cambio % en 1h:", cripto.get_percent_change_1h())
    print("Cambio % en 7d:", cripto.get_percent_change_7d())
    print("Precios en BTC:", cripto.get_price_btc())
    print("Capitalización de mercado en USD:", cripto.get_market_cap_usd())
    print("Volumen en 24h:", cripto.get_volume24())
    print("Volumen ajustado en 24h:", cripto.get_volume24a())
    print("Oferta circulante:", cripto.get_csupply())
    print("Oferta total:", cripto.get_tsupply())
    print("hola si")
    


if __name__ == "__main__":
    main()

