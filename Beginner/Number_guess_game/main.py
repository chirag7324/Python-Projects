"""Number Guess game project """
"""
step1 - 3 digits , 10-number of guess
step2 - secret number (random)
step3 - player guess the number
step4 - clues/hints
step5 - match secret number amd guess
"""
import random

num_digit = 3  # try it with 1 to 10 digits
max_guesses = 10


def main():
    """Main loop for game"""
    print(f''' Number Guess, is deductive logic game
    introduce by Chirag Patel , getmoregyan@gmail.com
    
    I am thinking of a {num_digit}-digit number with no repeated digit.
    Try to guess what it is. Here are some clues:
    When i say:     That means:
    correct         One digit is correct but in the wrong position
    correct_plus    One digit is correct and in the right position
    wrong           No digit is correct.
    
    For example if the secret number was 248 and your guess 843, then
    clues would be correct,correct_plus.
    ''')

    """Main loop start here"""
    while True:
        # first we need secret number
        secret_num = get_secret_num()
        print("I have thought up a number.")
        print(f"You have {max_guesses} guesses to get it.")

        num_guess = 1
        while num_guess <= max_guesses:
            guess = ''
            # Keep looping over until player enter a valid guess
            while len(guess) != num_digit or not guess.isdecimal():
                print(f"Guess#{num_guess}: ")
                guess = input('> ')
            clues = get_clues(guess, secret_num)
            print(clues)
            num_guess += 1
            if guess == secret_num:
                break
            if num_guess > max_guesses:
                print("You run out of guesses.")
                print(f"The answer was {secret_num}.")

        # Ask player if they want to play again
        print('Do you want to play again? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    print("Thank you for playing!")


def get_secret_num():
    """Return string madeup of three-digit"""
    numbers = list('0123456789')
    random.shuffle(numbers)

    secret_num = ''
    for i in range(num_digit):
        secret_num += numbers[i]
    return secret_num


def get_clues(guess, secret_num):
    """Return clues to the player according to description"""
    if guess == secret_num:
        return "Congratulation !!!! You won the game"

    clues = []
    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append('correct_plus')
        elif guess[i] in secret_num:
            clues.append('correct')
    if len(clues) == 0:
        return 'wrong'
    else:
        clues.sort()
        return ','.join(clues)


if __name__ == '__main__':
    main()

