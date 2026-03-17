from .objeto import Objeto

class Papel(Objeto):
    def __init__(self, cor):
        super().__init__(cor)

    def get_funcao(self):
        return "Mata pedras"
    
    def get_tipo(self):
        return "papel"