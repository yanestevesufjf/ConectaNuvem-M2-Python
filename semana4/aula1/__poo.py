# Definindo uma classe carro

class Carro:
    def __init__(self, marca = "", modelo = "", ano = ""):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

# Criando uma instância de Carro (Objeto)
vw_nivus = Carro('VW', 'Nivus', 2020)
