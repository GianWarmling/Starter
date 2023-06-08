from pessoa1 import Pessoa1
from pessoa2 import Pessoa2
from pessoa3 import Pessoa3

abacate = Pessoa1(
                input('Digite seu Nome: '),
                input('Digite seu Sobrenome: '),
                input('Digite sua Idade: '),
                input('Digite seu Peso: '),
                input('Digite seu Telefone: '),
                input('Digite seu Cpf: ')
                )


laranja = Pessoa2()

moranguinho = Pessoa3()

laranja.Nome = abacate.Nome
laranja.Sobrenome = abacate.Sobrenome
laranja.Idade = abacate.Idade
laranja.Peso = abacate.Peso
laranja.Telefone = abacate.Telefone
laranja.Cpf = abacate.Cpf

moranguinho.Nome = laranja.Nome
moranguinho.Sobrenome = laranja.Sobrenome
moranguinho.Idade = laranja.Idade
moranguinho.Peso = laranja.Peso
moranguinho.Telefone = laranja.Telefone
moranguinho.Cpf = laranja.Cpf

print(moranguinho)