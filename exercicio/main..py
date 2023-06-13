from conta import Conta

v = "*"*20

print(v, "Menu conta 1", v)

def menu():

  conta = Conta(
            input("Digite Seu Nome >> "),
            int(input("Digite O numero da conta >> ")),
            float(input("Digite o saldo da sua conta >> ")),
            float(input("Digite o limite >> "))
              )

  menu = 1

  while menu != 0:

    print('O que você deseja?')

    var = int(input('Digite:\n1-Extrato:\n2-Sacar:\n3-Depositar:\n4-Transferir:\n>>> '))
    
    match var:
      case 1:
        print(v,"Extrato conta 1", v)
        conta.extrato()

      case 2:
        conta.sacar(float(input("Digite o valor do saque >> ")))
        print(v,"Extrato Saque conta 1", v)
        conta.extrato()

    
      case 3:
        conta.depositar(float(input("Digite o valor do Deposito >> ")))
        print(v,"Extrato Deposito conta 1", v)
        conta.extrato()

      case 4:
        conta1 = Conta(
                    input("Digite o Nome >> "),
                    int(input("Digite o numero da conta >> ")),
                    float(input("Digite o saldo da sua conta >> ")),
                    float(input("Digite o limite >> "))
                      )

        print(v,"Extrato transferencia", v)

        conta1.transferir(float(input("Digite o valor da transferencia >> ")), conta,  conta1)
        print(v,"Extrato transeferencia conta 2", v)
        conta1.extrato()

        print(v,"Extrato transferencia", v)

        print(v,"Extrato transferencia conta 1", v)
        conta.extrato()

    menu = int(input("Você deseja sair?\n1 - Para Continuar\n0 - Para Sair\n"))

menu()