while True:
    palavra = input('Digite uma palavra: ')
    if palavra.lower() == 'sair':
        print('Fim')
        break
    if len(palavra) < 2:
        print('Palavra curta.')
        continue
    print('Tente digitar \"sair\"')



lista = [ 1, 2, 3, 4, 5 ]

for item in lista:
    if item % 2 == 0:
        print('{0} - Número par'.format(item))
        continue
    print('{0} - Número ímpar'.format(item))
    



