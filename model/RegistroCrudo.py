"""
operaciones para guardar los datos en un archivo txt
"""

from Cripto import Cripto

class Registro():
    def __init__(self):
        cripto = Cripto()


    def criptoObtenida(self):
        criptoObtenida = self.cripto.getAllids()
        return criptoObtenida
    
    def criptoNueva(self):
        pass