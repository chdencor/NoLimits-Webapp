from app.models.Cripto import Cripto
from app.models.RegistroCrudo import Registro



cripto = Cripto()
ids_obtenidos = cripto.getAllids()
    
# Crea una instancia de la clase Registro y actualiza los datos
registro = Registro()
registro.actualizar_cripto(ids_obtenidos)
print("Datos actualizados y guardados en JSON.")
