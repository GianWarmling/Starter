class Cliente:
    def __init__(self):
        
        self.Nome : str
        self.Sobrenome : str
        self.Idade : int
        self.Telefone : int

    def __str__(self):
        return f'{self.Nome} {self.Sobrenome} {self.Idade} {self.Telefone}'
