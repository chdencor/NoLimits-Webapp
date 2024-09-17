from app.models.Cripto import Cripto
from app.models.RegistroCrudo import Registro

cripto = Cripto()
idsObtenidos = cripto.getAllIds() 

registro = Registro()
registro.actualizarCripto(idsObtenidos)
print("Datos actualizados y guardados en JSON.")
