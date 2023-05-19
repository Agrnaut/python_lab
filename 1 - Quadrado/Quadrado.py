class Quadrado:
    def __init__(self, tamanho_lado):
        self._tamanho = tamanho_lado

    def muda_tamanho_lado(self, novotamanho):
        self._tamanho = novotamanho

    @property
    def mostra_e_calcula(self):
        return print("O lado é {} | A area é {}".format(self._tamanho, round(self._tamanho * self._tamanho, 3)))

