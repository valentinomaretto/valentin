print("Adivina el numero con amigos")
infinito=1
while infinito < 2:
    number_to_guess=int(input("put a number"))
    guesser=int(input("Guess the number"))
    if number_to_guess == guesser:
        print("you win")
    elif not number_to_guess == guesser:
        print("Try again")





