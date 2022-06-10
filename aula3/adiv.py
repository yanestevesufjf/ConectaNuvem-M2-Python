from random import randint, seed

total_tentativas = 1
seed(1)
numero_secreto = randint(0, 50)
acertou = False

while total_tentativas <= 3:
    chute = int(input(f"Tentativa {total_tentativas} - Informe um número: "))
    
    if chute == -1:
        print('Você desistiu do jogo')
        break
    
    if chute == numero_secreto:
        print('Você acertou')
        acertou=True
        break

    total_tentativas+=1

if acertou == False:
    print(f'Você perdeu, o número era {numero_secreto}')