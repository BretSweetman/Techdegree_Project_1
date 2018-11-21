import random

def start_game():
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print("Number Guessing Game!!")
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print("::::::Good Luck!::::::")
    print("~~~~~~~~~~~~~~~~~~~~~~")

    begin = input("Are you ready to begin?\n[Y or N]: ")
    if begin.lower().startswith("y"):
        start = True
    if not begin.lower().startswith("y"):
        start = False
        print("Have a nice day.")

    guess_the_number = random.randint(1, 10)
    num_guess = 1

    while start:
        try:
            guess = int(input("Guess a number 1-10: "))
            if guess > 10:
                raise NameError("Guess a number 1 through 10")
            elif guess < 1:
                raise NameError("Guess a number 1 through 10")

        except NameError:
            print("Please enter a digit 1 through 10.")
        except ValueError:
            print("Please enter a digit 1 through 10.")

        else:
            if guess > guess_the_number:
                print("It's Lower: ")
            elif guess < guess_the_number:
                print("It's Higher: ")
            elif guess == guess_the_number:
                print("~~~~~~~GAMER OVER~~~~~~~~\nWELL DONE! it took {} tries.".format(num_guess))
                play_again = input("Play Again? [Y or N]: ")
                guess_the_number = random.randint(1, 10)
                if play_again.lower().startswith("y"):
                    num_guess = 1
                    continue
                else:
                    print("Thanks for playing! See you next time!")
                    break

        num_guess += 1


if __name__ == '__main__':
    start_game()