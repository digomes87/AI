print("Bem vindo ao jogo")
numero_secreto = 42

chute = input("Digite o seu numero: ")
print("Voce digitou ", chute)


if numero_secreto == int(chute):
    print("Acertou misseravel")
else:
    print("Mais sorte na proxima")