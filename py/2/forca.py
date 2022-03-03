import random


def jogar():
    msg()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not enforcou and not acertou:
        chute = chute_jogador()

        if chute in palavra_secreta:
            marca_chute(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    resultado(acertou)


def resultado(acertou):
    if acertou:
        print("Venceu o Game")
    else:
        print("Tente Novamente !")


def marca_chute(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if chute == letra:
            letras_acertadas[index] = letra
        index += 1


def chute_jogador():
    chute = input('Qual letra ? ')
    chute = chute.strip().upper()
    return chute


def msg():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra_secreta):
    """
    # list Comprehensions
    """
    return ["_" for letra in palavra_secreta]


if __name__ == "__main__":
    jogar()
