# Exemplo de classe com definição de um construtor (__init__)

class Calculadora:

    def __init__(self,a, b):
        self.a = a
        self.b = b

    def soma(self):
        return self.a + self.b

    def subtrai(self):
        return self.a - self.b

    def multiplica(self):
        return self.a * self.b

    def divide(self):
        if (self.b == 0): return None
        return self.a / self.b


# conta = Calculadora(5, 5)
# print(conta.soma())
# print(conta.subtrai())
# print(conta.multiplica())
# print(conta.divide())