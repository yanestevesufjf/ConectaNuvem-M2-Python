set1 = { 24, 19, 43}

# inserindo um novo elemento
set1.add(9)
# inserindo + de 1 elemento
set1.update([12, 8])

# removendo um item, 
# retornará um erro caso o item não existir
set1.remove(8)

# # outra opção ao remove
set1.discard(99)

print(set1)

# como os sets não são ordenados, então, ao usar o método pop(), 
# não se saberá qual item será removido.
set1.pop()



print(set1)


# # declarando set de forma implicita
# set1 = {1, 2, 3}
# # declaração explicita
# set2 = set([1,2,3])

# print(set1)
# print(type(set1))


