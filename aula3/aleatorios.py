from random import randint, seed, randrange, \
                   choice, shuffle, sample, random

# lista_numeros = []
# for item in range(0, 6):
#     numero = randint(0, 60)
#     if numero in lista_numeros:
        

# seed(2) #inicia a semente dos número pseudo randômicos
for item in range(0, 10):
    print(randint(0, 20))

print(randint(0, 20)) # número "aleatório" de 0 a 20

# gerando uma lista com 5 numeros aleatórios
randomlist = sample(range(10, 30), 5) 
print('Random List')
print(randomlist)

print('Aleatórios pares:')

print(randrange(0, 50, 2)) # Pega um num par entre 0 e 50
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('Embaralhar lista:')
shuffle(items) # embaralha os itens da lista
print(items)

print('Escolhendo um item da lista de forma aleatória')
print(choice(items))



