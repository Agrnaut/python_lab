class Retangulo:
    def __init__(self, ladoa, ladob):
        self._ladoa = ladoa
        self._ladob = ladob


    @property
    def mostra_lados(self):
        return self._ladoa, self._ladob

    def novos_lados(self, novoladoa, novoladob):
        self._ladoa = novoladoa
        self._ladob = novoladob

    @property
    def calcular_area(self):
        return float(round(self._ladoa * self._ladob, 2))

    @property
    def calcular_per(self):
        return float(self._ladoa * 2 + self._ladob * 2)

    def calcular_cm2(self):
        return float(self._ladoa * self._ladob)