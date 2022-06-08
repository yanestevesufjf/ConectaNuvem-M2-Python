# Aula 1 - 07/06/2022

def somar(a, b):
    return a + b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

def sub(a, b):
    return a - b

def mostraMenu():        
    operacao = int(input("""Leve em conta as seguintes opções
        [1] Somar
        [2] Subtrair
        [3] Dividir
        [4] Multiplicação
    """))

    a = int(input('Informe um número (1): \n'))
    b = int(input('Informe um número (2): '))

    if operacao == 1:
        print(somar(a, b))
    elif operacao == 2:
        print(sub(a, b))
    elif operacao == 3:
        print(div(a, b))
    elif operacao == 4:
        print(mult(a, b))
    else:
        print('não é operação válida')

while True:
    mostraMenu()
    continua = int(input("Continuar com outra operação? [1 - Sim | 2 - Não)"))
    if continua != 1:
        break;

input()


# 
# var = "Yan"
# def nomeFuncao():
#     # var = "João"
#     global var
#     var = "João"    
#     print(var)

# print('Olá Mundo')
# nomeFuncao()
# print('--- global ---')
# print(var)






# var = "Yan"
# var = 5
# if var >= 5:
#     print('')
