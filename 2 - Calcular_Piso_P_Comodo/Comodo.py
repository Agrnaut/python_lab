class Comodo:
    def __init__(self, comprimento, largura):
        self._comprimento = comprimento
        self._largura = largura


    def calcula_m2(self):
        return (float(self._comprimento * self._largura))