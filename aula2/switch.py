def meu_switch(opcao):
    opcoes = {
        0: "Você escolheu zero",
        1: "Você escolheu 1",
        2: "Você escolheu 2",
    }
    return opcoes.get(opcao, "Opção inválida.")    

if __name__ == "__main__":
    opcao = int(input("Informe um número de 0 a 2: "))
    print (meu_switch(opcao))