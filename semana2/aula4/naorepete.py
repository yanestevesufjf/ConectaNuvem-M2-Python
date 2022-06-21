from random import randint


# for i in range(0, 10):
#     numero = randint(0, 20)
#     if not numero in lista:
#         lista.append(numero)
lista = []

lista2 = []
while True:
    numero = randint(0, 20)
    lista.append(numero)
    lista2.append(numero)
    lista2 = list(set(lista2))
    if len(lista2) == 10:
        break
print(lista)
print(lista2)