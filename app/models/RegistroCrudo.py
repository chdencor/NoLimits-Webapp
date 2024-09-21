"""
Operaciones para guardar los datos en un archivo txt
"""

from app.models.Cripto import Cripto
import os
import json

class Registro:
    def __init__(self):
        self.archivo = "criptos.json"
        self.criptoRegistrado = self._loadFromFile()

    def _loadFromFile(self):
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    data = json.load(file)
                    # Asegúrate de que las claves necesarias estén presentes
                    if 'idsRegistrados' not in data:
                        data['idsRegistrados'] = []
                    if 'idsNuevos' not in data:
                        data['idsNuevos'] = []
            except json.JSONDecodeError:
                data = {"idsRegistrados": [], "idsNuevos": []}
            except Exception as e:
                print(f"Error al cargar el archivo: {e}")
                data = {"idsRegistrados": [], "idsNuevos": []}
        else:
            data = {"idsRegistrados": [], "idsNuevos": []}
        return data


    def _saveToFile(self):
        """
        Guarda los datos actuales en el archivo JSON.
        """
        try:
            with open(self.archivo, 'w') as file:
                json.dump(self.criptoRegistrado, file, indent=4)
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

    def criptoNueva(self):
        """
        Obtiene la lista de IDs nuevos.
        """
        return self.criptoRegistrado.get('idsNuevos', [])

    def actualizarCripto(self, idsObtenidos):
        """
        Actualiza el registro con nuevos IDs y guarda los cambios.
        
        :param idsObtenidos: Lista de IDs de criptomonedas obtenidas.
        """
        # Obtén los IDs registrados
        idsRegistrados = set(self.criptoRegistrado.get('idsRegistrados', []))
        
        # Encuentra los IDs nuevos que no están en los registrados
        idsNuevos = list(set(idsObtenidos) - idsRegistrados)
        
        # Actualiza la lista de IDs registrados
        self.criptoRegistrado['idsRegistrados'].extend(idsNuevos)
        
        # Guarda los cambios en el archivo JSON
        self.criptoRegistrado['idsNuevos'] = idsNuevos
        self._saveToFile()
