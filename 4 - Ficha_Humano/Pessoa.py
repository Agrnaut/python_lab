class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self._nome = nome.title()
        self._idade = idade
        self._peso = peso
        self._altura = altura

    def envelhecer(self, nova_idade): #nova idade 30
        self._idade = nova_idade


    @property
    def mostra_pessoa(self):
        return self._nome, self._idade, self._peso, round((self._altura), 2)

    def engordar(self, novo_peso):
        self._peso = novo_peso


    def crescer(self, nova_altura):
        self._altura = nova_altura