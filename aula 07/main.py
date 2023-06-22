from conta import Conta

conta = Conta(input('Digite seu Nome: '),             
int(input('Digite seu Número: ')),
#atributo saldo conta
float(input('Digite seu Saldo Inicial: ')),
#atributo limite conta
float(input('Digite o limite da sua Conta: ')))

conta.limite = 3500

print(conta)
