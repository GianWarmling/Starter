class Conta:
    titular : str
    numero : int
    saldo : float
    limite : float

    def __str__(self):
        return f'{self.titular} - {self.numero} - {self.saldo} - {self.limite}'