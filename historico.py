import datetime


class Historico:

    # slots define quais os atributos serão criados na instancia da classe
    # OBS: Qualquer atributo da instancia da classe que nao esteja definido no slot nao sera permitido
    __slots__ = ['_data_abertura', '_transacoes']

    def __init__(self):
        self._data_abertura = datetime.datetime.today()
        self._transacoes = []

    @property
    def data_abertura(self):
        return self._data_abertura

    @data_abertura.setter
    def data_abertura(self, date):
        self._data_abertura = date

    @property
    def transacoes(self):
        return self._transacoes

    @transacoes.setter
    def transacoes(self, value):
        self._transacoes = value

    def imprime(self):
        print(f'data abertura: {self.data_abertura}')
        print('transacoes: ')
        for t in self.transacoes:
            print('-', t)

    def data_atual(self):
        return f'{datetime.datetime.today()}'


'''
    def log_saque(self, valor):
        self.transacoes.append(f'{self.data_atual()} - Saque de R${valor} Reais')

    def log_deposito(self, valor):
        self.transacoes.append(f'{self.data_atual()} - Deposito de R${valor} Reais')

    def tranferencia(self, remetente, destino, valor):
        # inserir no historico do remetente
        self.transacoes.append(f'{self.data_atual()} - Transferencia efetuada de R${valor} para {destino.titular.nome}')
        # inserir no historico destino
        destino.transacoes.append(f'{self.data_atual()} - Transferencia recebida de R${valor} - Remetente - {remetente.titular.nome}')

'''
