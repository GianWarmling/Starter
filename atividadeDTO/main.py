#DTO - DATA TRANFERS OBJECT
from pessoa import Pessoa
from funcionario import Funcionario
from cliente import Cliente
from animal import Animal
from paidepet import Paidepet

var1 = Pessoa(
            input('Digite seu Nome: \n'),
            input('Digite seu Sobrenome: \n'),
            input('Digite sua Idade: \n'),
            input('Digite seu CPF: \n'),
            input('Digite seu Telefone: \n'),
            input('Digite o código da Carteira de Trabalho: \n'),
            input('Digite sua Profissão: \n')
)

var2 = Funcionario()

var3 = Cliente()

var4 = Animal(
            input('Digite o Nome do Pet: '),
            input('Digite o tipo: '),
            input('Digite a raça: '),
            input('Digite a cor: ')
)

var5 = Paidepet()

var2.Nome = var1.Nome
var2.Sobrenome = var1.Sobrenome
var2.Idade = var1.Idade
var2.Telefone = var1.Telefone

var3.Nome = var2.Nome
var3.Sobrenome = var2.Sobrenome
var3.Idade = var2.Idade
var3.Telefone = var2.Telefone

var5.Nome = var1.Nome
var5.Nomepet = var4.Nomepet
var5.Tipo = var4.Tipo

print('='* 20, 'Menu de Dados - Pessoa', '='* 20, '\n')
print(var1.Nome)
print(var1.Sobrenome)
print(var1.Idade)
print(var1.Cpf)
print(var1.Telefone)
print(var1.Carteiradetrabalho)
print(var1.Profissao)
print('\n')

print('='* 20, 'Menu de Dados - Funcionario', '='* 20, '\n')
print(var2.Nome)
print(var2.Sobrenome)
print(var2.Idade)
print(var2.Telefone)
print('\n')

print('='* 20, 'Menu de Dados - Cliente', '='* 20, '\n')
print(var3)
print('\n')

print('='* 20, 'Menu de Dados - Animal', '='* 20, '\n')
print(var5.Nome)
print(var5.Nomepet)
print(var5.Tipo)
print(var4.Raca)
print(var4.cor)