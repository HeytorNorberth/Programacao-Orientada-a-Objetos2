class Cliente:

    # slots define quais os atributos serão criados na instancia da classe
    # OBS: Qualquer atributo da instancia da classe que nao esteja definido no slot nao sera permitido
    __slots__ = ['_nome', '_sobrenome', '_cpf']

    def __init__(self, nome, sobrenome, cpf):
        self._nome = nome
        self._sobrenome = sobrenome
        self._cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, name):
        self._nome = name

    @property
    def sobrenome(self):
        return self._sobrenome

    @sobrenome.setter
    def sobrenome(self, lastname):
        self._sobrenome = lastname

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, cpf):
        self._cpf = cpf
