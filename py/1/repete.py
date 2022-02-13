import random
print('##################################')
print('Bem vindo ao jogo')
print('##################################')

numero_secreto = round(random.randrange(1, 101))
tentativas = 3
print('QUal o nivel de dificuldade')
print('(1) FAcil')
print('(2) medio')
print('(3) Hard')

nivel = int(input('Tua escolha: '))

if nivel == 1:
    total_de_tentativas = 20
elif nivel == 2:
    total_de_tentativas = 10
else:
    total_de_tentativas = 5


for tentativas in range(1, total_de_tentativas + 1):
    print("Tentativas: {}".format(tentativas))

    chute_str = input('Digite um número: ')
    print('Você digitou: ', chute_str)
    chute = int(chute_str)

    if chute < 1 or chute > 100:
        print('Digite um número entre 1 e 100')
        continue

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if acertou:
        print('Acertou !!!')
        break
    else:
        if maior:
            print('Errou, chute acima do numero secreto')
        elif menor:
            print('Erro, chute a abaixo do numero secreto')


print('Fim de jogo')
