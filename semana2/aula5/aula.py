from collections import namedtuple

Estados = namedtuple('Estados', ['sigla', 'nome', 'regiao'])

estado_rj = Estados('rj', 'rio de janeiro', 'sudeste')
estado_sc = Estados('sc', 'santa catarina', 'sul')
estado_mg = Estados('mg', 'minas gerais', 'sudeste')

lista_estados = [estado_rj, estado_mg, estado_sc]

for item in lista_estados:
    if item.regiao == 'sudeste':
        print(f'{item.sigla} pertence ao sudeste')