"""
operaciones para guardar los datos en un archivo txt
"""

from Cripto import Cripto
import os
import json

class Registro:
    def __init__(self):
        self.archivo = "criptos.json"
        self.cripto_registrado = self._load_from_file()

    def _load_from_file(self):
        """
        Carga los datos del archivo JSON. Si el archivo no existe o tiene errores,
        retorna un diccionario con una lista de IDs registrados.
        """
        if os.path.exists(self.archivo):
            try:
                with open(self.archivo, 'r') as file:
                    data = json.load(file)
            except json.JSONDecodeError:
                # El archivo JSON está corrupto o malformado
                data = {"ids_registrados": []}
            except Exception as e:
                # Manejar otros posibles errores
                print(f"Error al cargar el archivo: {e}")
                data = {"ids_registrados": []}
        else:
            # Archivo no existe, se crea uno nuevo
            data = {"ids_registrados": []}
        return data

    def _save_to_file(self):
        """
        Guarda los datos actuales en el archivo JSON.
        """
        try:
            with open(self.archivo, 'w') as file:
                json.dump(self.cripto_registrado, file, indent=4)
        except Exception as e:
            print(f"Error al guardar el archivo: {e}")

    def cripto_nueva(self):
        """
        Obtiene la lista de IDs nuevos.
        """
        return self.cripto_registrado.get('ids_nuevos', [])

    def actualizar_cripto(self, ids_obtenidos):
        """
        Actualiza el registro con nuevos IDs y guarda los cambios.
        
        :param ids_obtenidos: Lista de IDs de criptomonedas obtenidas.
        """
        # Obtén los IDs registrados
        ids_registrados = set(self.cripto_registrado.get('ids_registrados', []))
        
        # Encuentra los IDs nuevos que no están en los registrados
        ids_nuevos = list(set(ids_obtenidos) - ids_registrados)
        
        # Actualiza la lista de IDs registrados
        self.cripto_registrado['ids_registrados'].extend(ids_nuevos)
        
        # Guarda los cambios en el archivo JSON
        self.cripto_registrado['ids_nuevos'] = ids_nuevos
        self._save_to_file()


if __name__ == "__main__":



    cripto = Cripto()
    ids_obtenidos = cripto.getAllids()
    
    # Crea una instancia de la clase Registro y actualiza los datos
    registro = Registro()
    registro.actualizar_cripto(ids_obtenidos)
    print("Datos actualizados y guardados en JSON.")
