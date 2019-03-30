secret_word = "queen"
guesser = ""
init = 0
max = 3
out_of_guess = False

while guesser != secret_word and not out_of_guess:
    if init < max:
        guesser = input("Enter guess:")
        init += 1
    else:
        out_of_guess = True

if out_of_guess:
    print("Out of guesses, You Lose!")

else:
    print("Congratulation, You Win!")
