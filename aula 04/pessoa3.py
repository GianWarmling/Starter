class Pessoa3:
        def __init__(self):   

            self.Nome : str 
            self.Sobrenome : str 
            self.Idade : int 
            self.Peso : float
            self.Telefone : int
            self.Cpf : int

        def __str__(self):
            return f'{self.Nome} {self.Sobrenome} {self.Idade} {self.Peso} {self.Telefone} {self.Cpf}'