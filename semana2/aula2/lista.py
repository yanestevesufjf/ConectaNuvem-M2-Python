lista = [7, 3, 5, 7, 9, 12, 423, 31, 324, 213, 323, 121, -7, -6450, -392, -131]

print('Menor item da lista: ')
print(min(lista))

print('Maior item da lista: ')
print(max(lista))

print('Quantidade de itens na lista: ')
print(len(lista))

# Adicionando um elemento ao final da lista
print('Adicionando um elemento ao final da lista')
lista.append(1293)
print(lista)

# Adicionando o número 1 na posição 0 da lista
print('Adicionando o número 1 na posição 0 da lista')
lista.insert(0, 1)
print(lista)

# Removendo o último item da lista (1293)
print('Removendo o último item da lista (1293)')
lista.pop()
print(lista)

# Removendo o elemento da posição 3 da lista
print('Removendo o elemento da posição 3 da lista')
lista.pop(3)
print(lista)

# Removendo o primeiro elemento igual a 12 
print('Removendo o primeiro elemento igual a 12 ')
lista.remove(12)
print(lista)