"""
Clase Cripto que contiene todos los metodos
para recuperar la informacion de las criptomonedas.
"""

from APICripto import APICripto

class Cripto:
    def __init__(self):
        self.data = APICripto()
        self.respuesta = self.data.APICall(self.data.url)  # Llamada a la API

    def get_Ids(self):
        # Convertimos la respuesta a JSON
        parsed_response = self.data.APIParsing(self.respuesta)
        
        # Usamos la respuesta parseada para obtener los datos
        dataRetrieved = self.data.getKeyValue(parsed_response)

        ids = [item.get("id") for item in dataRetrieved]  # Acceder a cada "id" en los datos
        return ids
    
    

def main():
    cripto = Cripto()
    ids = cripto.get_Ids()
    if ids:
        print(ids)

if __name__ == "__main__":
    main()
