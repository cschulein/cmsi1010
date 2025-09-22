attempts = 0
def reset_game():
    global attempts
    attempts = 0
    number_guesser()

def get_random_num(x, y):
    import random
    return random.randint(x, y)
def guess_check(guess, num):
    global attempts
    global x
    x = False
    if guess < num:
        print("Too low! Guess Again")
        attempts += 1
        return False
    elif guess > num:
        print("Too high! Guess Again")
        attempts += 1
        return False
    else:
        attempts += 1
        print("Congratulations! You guessed the number!")
        print("It took you", attempts, "attempts to guess the number.")
        reset_game()
        x = True
        return True
def number_guesser():
    global attempts
    attempts = 0
    global x
    x = False
    num = get_random_num(1, 1000)
    print("Guess a number between 1 and 1000. Type 'bye' or 'exit' to quit.")
    while x == False:
        guess = input("Enter your guess: ")
        if guess.lower() == 'bye' or guess.lower() == 'exit':
            print("Thanks for playing! Goodbye!")
            break
        elif not guess.isdigit():
            print("Please enter a valid number.")
        else:
            guess_check(int(guess), num)
number_guesser()
        