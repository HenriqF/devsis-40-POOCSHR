from .objeto import Objeto

class Pedra(Objeto):
    def __init__(self, cor):
        super().__init__(cor)

    def get_funcao(self):
        return "Mata tesouras"
    
    def get_tipo(self):
        return "pedra"