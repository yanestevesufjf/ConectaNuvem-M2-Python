class Felino:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor
    def comer(self):
        print('Felino come')

class Animal:
    def __init__(self, nome, cor):
        self.nome = nome
        self.cor = cor

    def comer(self):
        print('Animal come')

    # def bonificacao(self):
    #     print(self.salario)
    #     self.salario = _double * self.salario +...

class Gato(Felino, Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)
        # super().comer()

gato = Gato('Pandora', 'preto')    
# gato.comer()