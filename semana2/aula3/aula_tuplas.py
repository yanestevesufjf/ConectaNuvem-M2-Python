from collections import namedtuple

Pai = namedtuple('Pai', ['nome', 'filhos'])
pai_marcelo = Pai('Marcelo', ['abel', 'raul'])
print(pai_marcelo.filhos)

Estados = namedtuple('Estados', ['sigla', 'nome'])
estado_rj = Estados('rj', 'rio de janeiro')
print('-- elemento estado rj --')
print(estado_rj[0])

tupla = ('element1', 'element2')
# tupla com 1 elemento
# tupla = ('element1',)

# capturando o tipo da variável
# # print(type(tupla))