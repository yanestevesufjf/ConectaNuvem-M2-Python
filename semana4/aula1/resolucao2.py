# Construir uma aplicação que contenha uma classe pai chamada funcionário e 3 classes filhas, desenvolvedor, 
# designer e gerente de marketing. Implemente na classe 
# pai (Funcionários), os seguintes métodos: setarSalario (valor inteiro, ex: 4500), 
# aumentarSalario (por porcentagem) e demitir (flag vinculado=True/False). 
# E para a classe do gerente de marketing, adicione o método “bonificacao” que aumenta o 
# salário do funcionário de acordo com a porcentagem passada por argumento.
# Inicialize o sistema com 1 funcionário para cada grupo presente e defina como atributos seus nomes e salários.

class Funcionario:
    def __init__(self, nome, salario, vinculo = True):
        self.__salario = salario
        self.vinculo = vinculo
        self.nome = nome

    def setarSalario(self, salario):
        self.salario = salario

    def aumentoSalario(self, percent):
        self.salario = self.salario * percent + self.salario    

    def demitir(self):
        self.vinculo = False
        print('O funcionário ...')

class Dev(Funcionario):
    def __init__(self, nome, salario, vinculo=True):
        super().__init__(nome, salario, vinculo)


class Designer(Funcionario):
    def __init__(self, nome, salario, vinculo=True):
        super().__init__(nome, salario, vinculo)

class Mkt(Funcionario):
    def __init__(self, nome, salario, vinculo=True):
        super().__init__(nome, salario, vinculo)

    def bonificacao(self, percent):
        if self.vinculo == False:
            print('O usuário não faz parte da empresa')
            return
        self.salario = self.salario * percent + self.salario            
        print(f'O novo salario do {self.nome}, com bonificação, é {self.salario}')

dev = Dev('Yan', 12000)
designer = Designer('Gabriel', 7000)
mkt = Mkt('Wagner', 13000)

mkt.demitir()

mkt.bonificacao(0.35)


