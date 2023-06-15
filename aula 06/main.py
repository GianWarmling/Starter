from conta import Conta

conta = Conta(input('Digite seu Nome: '),

#atributo saldo conta
float(input('Digite seu Saldo Inicial: ')),
#atributo limite conta
float(input('Digite o limite da sua Conta: ')))

print(conta)

conta.set_titular(input('Digite o novo Nome: '))

conta.set_saldo(float(input('Digite seu novo saldo: ')))

conta.set_limite(float(input('Digite seu novo Limite: ')))

print('O novo titular é: {}'.format(conta.get_titular()))

print('O novo saldo é: {}'.format(conta.get_saldo()))

print('O novo limite é: {}'.format(conta.get_limite()))