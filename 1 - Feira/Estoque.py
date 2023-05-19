
class Feira:
    def __init__(self, nome_fruta):
        self._nome_fruta = nome_fruta


    def __getitem__(self, item):
        return self._nome_fruta[item]

    @property
    def nome_fruta(self):
        return self._nome_fruta

    # @nome.setter
    # def nome(self, nome):
    #     self.nome = nome

class Solicitante:
    def __init__(self, nome):
        self._nome_solicitante = nome.title()

    @property
    def nome(self):
        return self._nome_solicitante


