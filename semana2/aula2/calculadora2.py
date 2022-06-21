# Exemplo de classe sem a definição de um construtor (__init__)

class Calculadora:
    def soma(self, a, b):
        return a + b
    
    def subtrai(self, a, b):
        return a - b

    def multiplica(self, a, b):
        return a * b

    def divide(self, a, b):
        if (b == 0): return None
        return a / b


conta = Calculadora()
print(conta.soma(5, 2))
print(conta.multiplica(3, 3))
print(conta.subtrai(6, 4))
print(conta.divide(12, 3))