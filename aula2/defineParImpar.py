def defineParImpar(x):
    if x % 2 == 0:
        print('é par')
        return
    print('é impar')


while True:
    numero = int(input('Informe um número\n'))
    if numero == -1: # ao digitar -1 o programa será encerrado
        break
    defineParImpar(numero)