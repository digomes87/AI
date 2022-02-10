print('##################################')
print('Bem vindo ao jogo')
print('##################################')

numero_secreto = 42
tentativas = 3


while(tentativas > 0):
    print("Tentativas: {}".format(tentativas))
    tentativas = tentativas - 1

    chute_str = input('Digite um número: ')
    print('Você digitou: ', chute_str)
    chute = int(chute_str)
    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if(acertou):
        print('Acertou !!!')
    else:
        if(maior):
            print('Errou, chute acima do numero secreto')
        elif(menor):
            print('Erro, chute a abaixo do numero secreto')



print('Fim de jogo')