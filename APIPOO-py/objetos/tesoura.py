from abc import *
from .objeto import Objeto

class Tesoura(Objeto):
    def __init__(self, cor):
        super().__init__(cor)

    def get_funcao(self):
        return "Mata papeis"
    
    def get_tipo(self):
        return "tesoura"