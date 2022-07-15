from historico import Historico


class Conta:

    # slots define quais os atributos serão criados na instancia da classe
    # OBS: Qualquer atributo da instancia da classe que nao esteja definido no slot nao sera permitido
    __slots__ = ['_numero', '_titular', '_saldo', '_limite', '_historico']

    _total_contas = 0

    # construtor da classe Conta
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo
        self._limite = limite
        self._historico = Historico()
        Conta._total_contas += 1

    # getters e setters
    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        self._numero = valor

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, name):
        self._titular = name

    @property
    def saldo(self):
        return self._saldo

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limit):
        self._limite = limit

    @property
    def historico(self):
        return self._historico

    # metodos da classe conta
    # Deposita da conta do usuario
    def deposita(self, valor):
        if valor <= 0:
            return False
        else:
            self._saldo += valor
            self.historico.transacoes.append(
                f'{self.historico.data_atual()} - Deposito de R${valor}')
            return True

    # Saca da conta do usuario
    def saca(self, valor):
        if valor <= 0:
            return False
        if self.saldo < valor:
            return False
        else:
            self._saldo -= valor
            self.historico.transacoes.append(
                f'{self.historico.data_atual()} - Saque de R${valor}')
            return True

    # extrato da conta -> imprime o numero da conta e o saldo presente nela
    def extrato(self):
        print(f'numero: {self.numero}\nSaldo: {self.saldo}\n')

    def transfere(self, destino, valor):
        if self.saca(valor):
            try:
                destino.deposita(valor)
                self.historico.transacoes.append(
                    f'{self.historico.data_atual()} -  Transferencia de {valor} para conta {destino.numero} - {destino.titular.nome}')
                destino.historico.transacoes.append(
                    f'{destino.historico.data_atual()} -  Transferencia de {valor} recebida da conta {self.numero} - {self.titular.nome}')
                return True
            except NameError:
                return False
        else:
            return False

    @staticmethod
    def get_total_contas():
        return Conta._total_contas
