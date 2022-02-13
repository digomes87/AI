def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = 'musica'

    enforcou = False
    acerto = False

    # precisa ser true para parar
    while not enforcou and not acerto:
        chute = input('Qual letra ? ')

        for letra in palavra_secreta:
            if chute == letra:
                print(chute)


        print('Continua ... ')

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
