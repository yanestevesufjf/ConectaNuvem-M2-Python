while True:
    palavra = input('Digite uma palavra: ')

    if palavra.lower() == 'sair':
        break

    if len(palavra) < 2:
        print('Palavra pequena')
        continue
    
    print('Para interromper digite \"sair\"')