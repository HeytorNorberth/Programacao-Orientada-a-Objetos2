# Orientação a objetos
# diz o arquivo e passa a classe
# importando uma classe de um arquivo pytohn
from copy import copy
from http import client
from cliente import Cliente
from conta import Conta


# criando um objeto da classe python que foi importando do arquivo conta.py
'''
conta = Conta('123456', 'Heytor Norberth', 500)
conta2 = Conta('654321', 'Chico Bala', 0)
'''

'''
if conta.saca(100):
    print('Saque efetuado')
else:
    print('Não foi possivel efetuar o saque!\n')
'''


# ponteiro com objeto
# Seja c1 e c2 objetos, se eu fizer c1 = c2, significa dizer que c1 e c2 apontam para o mesmo espaco de memoria
# Ou seja, oq modificar em um,modifica no outro, no caso de uma soma,vai mudar o numero independente se for somar com o c1 ou o c2

# forma segura de fazer uma copia, sem fazer o ponteiro entre eles


'''
c2 = copy(conta)

if conta.transfere(conta2, 10000):
    print('Transferencia efetuada')
else:
    print('Nao foi possivel efetuar a tranferencia')

'''

cliente = Cliente('Heytor Norberth', 'Leite da Silva', '12345678912')
conta_cliente = Conta('123-4', cliente, 120.0, 1000.0)

cliente2 = Cliente('Kauan', 'Norberth leite da silva', '4578965415')
conta_cliente2 = Conta('654-8', cliente2, 200.0, 1000.0)

# Sacar do cliente 01
print(f'Cliente01 - Saldo antes do saque: {conta_cliente.saldo}')
# saque de 20 reais
print('Saque de 20 reais')
conta_cliente.saca(20)
print(f'Cliente01 - Saldo depois do saque: {conta_cliente.saldo}\n')

# Deposito na conta do cliente 02
print(f'Cliente02 - Saldo antes do deposito: {conta_cliente2.saldo}')
print('Deposito de 40 reais')
conta_cliente2.deposita(40)
print(f'Cliente02 - Saldo depois do deposito: {conta_cliente2.saldo}\n')

# tranferencia do cliente01 para o cliente02
# saldo do cliente01
print(f'Cliente01 - Saldo antes da transferencia: {conta_cliente.saldo}')

# saldo do cliente02
print(f'Cliente02 - Saldo antes da transferencia: {conta_cliente2.saldo}')

print(f'Tranferencia de 50 reais de {cliente.nome} para {cliente2.nome}')
# Tranferencia do cliente01 para o cliente02
conta_cliente.transfere(conta_cliente2, 50)

# saldo do cliente01
print(f'Cliente01 - Saldo depois da transferencia: {conta_cliente.saldo}')
# saldo do cliente02
print(f'Cliente02 - Saldo depois da transferencia: {conta_cliente2.saldo}\n')

# imprimir o historico das conta01
print(
    f'Historico da conta do cliente 01 {conta_cliente.numero} - {conta_cliente.titular.nome}')
conta_cliente.historico.imprime()
print()

# imprimir o historico da conta02
print(
    f'Historico da conta do cliente 01 {conta_cliente2.numero} - {conta_cliente2.titular.nome}')
conta_cliente2.historico.imprime()

# imprimindo a quantidade de contas criadas
print(Conta.get_total_contas())

# Adicionando um novo cliente e uma nova conta
cliente3 = Cliente('Coité', 'Marabino', '4578965415')
conta_cliente3 = Conta('654-8', cliente2, 200.0, 1000.0)

# imprimindo a quantidade de contas criadas
print(Conta.get_total_contas())
