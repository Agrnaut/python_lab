class Quadrado:
    def __init__(self, tamanho_lado):
        self._tamanho = tamanho_lado

    @property
    def tamanho(self):
        return self._tamanho

    def calculo(self):
        return float(round(self._tamanho * self._tamanho, 3))

    def novo_tamanho(self, novotamanho):
        self._tamanho = float(novotamanho)