print("Bem vindo ao jogo")
secret_number = 42

guess = input("What is your number: ")
print("You Guess is ", guess)

guess = int(guess)

if secret_number == guess:
    print("Sorry, wrong !!")
else:
    if guess > secret_number:
        print("Your Number is Up")
    if guess < secret_number:
        print("Your Number is Down")
        
    print("Nice Tried !")
