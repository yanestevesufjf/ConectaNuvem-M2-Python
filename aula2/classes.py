class Cachorro:

    def __init__(self, nome = ""):
        self.nome = nome

    def setCor(self, cor):
        self.cor = cor

c1 = Cachorro("Buzzy")

c1.setCor('preto')

print('{0} - {1}'.format(c1.nome, c1.cor))

# print(f"... {c1.nome}")



