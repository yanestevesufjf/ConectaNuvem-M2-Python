from collections import namedtuple

# Definindo uma organização/estrutura para a tupla Estados
Estados = namedtuple('Estados', ['sigla', 'nome', 'regiao'])

estado_rj = Estados('RJ', 'Rio de Janeiro', 'Sudeste')
estado_sp = Estados('SP', 'São Paulo', 'Sudeste')
estado_sc = Estados('SC', 'Santa Catarina', 'Sul')

# concatenando tuplas
estados_br = estado_rj + estado_sp + estado_sc
print(estados_br)
# print(estado_rj[2]) # Sudeste
# print(estado_sc.sigla) # SC


# acessando elementos das tuplas
for x in estado_rj:
    print(x)

# # Passo um valor que seja iterável para "tuple"
# tupla_explicita = tuple([10,100,200])

# print(tupla_explicita)
# # Acessando indice 2 da tupla - número 200
# print(tupla_explicita[2])


# # Definição da tupla ocorre por parentêses
# tupla_numerica = (10, 100, 200)

# print(tupla_numerica)
# # Acessando indice 2 da tupla - número 200
# print(tupla_numerica[2])


