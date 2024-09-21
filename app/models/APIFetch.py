from abc import ABC
from abc import abstractmethod
import requests


"""
Crea una clase abstracta para las llamadas a la API.
Actua como API gateway para las APIs consumidas
"""
class APIFetch(ABC):
    def __init__(self, url):
        self.url = None
    
    def APICall(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            print("Error in API call. Status code: ", response.status_code)
            return None
    
    def APIParsing(self, response):
        jsonLoaded = response.json()
        return jsonLoaded
    
    @abstractmethod
    def getKeyValue(self, dictionary):
        pass