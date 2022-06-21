from random import choice
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

file = open('nomes.txt', 'r')
lista = file.readlines()
file.close()

palavra = choice(lista).split('\n')[0].lower()

lista_letras = []
lista_traco = []
lista_erro = []
tentativas = []
acertos = 0
chutarPalavra = -1

for i in range(len(palavra)):
    lista_letras.append(palavra[i])
    lista_traco.append('_')

# Dar o resultado de derrota caso o usuário 
# erre 10 letras.
while True:
    cls()
    if acertos == len(lista_letras):
        print('Parabéns. Você ganhou!')
        print(f'A palavra é \"{palavra}\"')
        break
    
    print(lista_traco)
    
    print('Tentativas: ' + str(tentativas))
    print('Erros: ' + str(lista_erro))

    letra = input('Informe uma letra para tentar descobrir a palavra: ')        
        
    tentativas.append(letra)
    
    c = lista_letras.count(letra)    
    if c > 0:
        print(f'Você acertou a letra {letra}')
        # lista_letras
        index_letra = 0
        for i in range(0, c):
            index_letra = lista_letras.index(letra, index_letra)
            lista_traco[index_letra] = letra
            index_letra+=1
            acertos+=1
        continue
    
    print(f'A letra {letra} não está presente na palavra.')
    lista_erro.append(letra)

    if len(lista_erro) == 10:
        print('Você perdeu')
        break


