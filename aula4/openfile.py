# file = open('numeros.txt', 'r') # read 
# lista = file.readlines()
# print(lista)

# file = open('numeros.txt', 'r')

# print(mylist)
# # lista = file.readlines()
# # print(lista)


with open('numeros.txt') as f:
    lista = f.read().splitlines() 

print(lista)
