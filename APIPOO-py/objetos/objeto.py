from abc import abstractmethod, ABC

class Objeto(ABC):
    def __init__(self, cor):
        self.cor = cor

    def get_cor(self):
        return self.cor

    @abstractmethod
    def get_funcao(self):
        pass

    @abstractmethod
    def get_tipo(self):
        pass