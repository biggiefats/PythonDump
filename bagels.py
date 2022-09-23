import random

# Imports the random module for specific purposes

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    # Rules:

    # Triple speech marks make the usage of \n unneccesary

    print('''I am thinking of a {}-digit number with no repeated digits.
    
    Try to guess what it is. Here are some clues:
    
    When I say (x) that means:
    Pico - One digit is correct but is in the wrong position.
    Fermi - One digit is correct and in the right position.
    Bagels - No digit is correct.
                       
    For example, if the secret number was 248 and your guess was 843, the
    clues would be Fermi Pico.
    '''.format(NUM_DIGITS))

    # 1st way to format variables into text:
    # - Add rich brackets (?) in string
    # - Use the .format function
    # - Insert the variable that you want to replace the rich brackets
    # - If you did it right, it should work!

    while True:
        secretNum = getSecretNum()
        print('I have thought of a number.')
        print(f'You have {MAX_GUESSES} guesses to get it.')

        # 2nd way to format variables into text:
        # - Add 'f' outside of string
        # - Add rich brackets into string
        # - Place variable into rich brackets
        # - If you did it right, it should work!

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                # While the length of your guess is not the
                # number of digits or your guess is not a
                # decimal,

                print("Guess # {}: ".format(numGuesses))
                guess = input('> ')

                # take a guess.

            clues = getClues(guess, secretNum)
            print(clues)

            # Tells user on Fermi and Pico numbers
            # as well as validity for Bagels

            numGuesses += 1

            if guess == secretNum:
                break

            # Function of break:
            # - Terminates the current loop if conditions met
            # - Branches to statements outside the loop that the break is contained in

            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}.'.format(secretNum))

        print('Do you want to play again? (yes or no)')
        if not input('>').lower().startswith('y'):
            break
    print('Thanks for playing!')


def getSecretNum():
    numbers = list('0123456789')
    random.shuffle(numbers)

    # Creates a list of digits from 0 to 9
    # Shuffles the numbers up with the random.shuffle function

    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

    # Return function sends back data to client/bot

    # Say, if a function called number_3() was made
    # and I returned the number 3 in the function,
    # when I call the function,
    # the function returns (prints) the number 3.

    # Pretend number_3() = x.
    # If I wanted to find out what 3 * 2 is,
    # I would write either:
    # - number_3() * 2
    # OR
    # - x * 2 (due to us theoretically making the variable 'x' = number_3())

    # We can manipulate a value by calling the function!


def getClues(guess, secretNum):
    # Returns the string with the PicoFermiBagels clues for a guess
    # and a secret number pair

    if guess == secretNum:
        return 'You got it!'

    clues = []

    # List in which clues will be added

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Fermi')

        # If the index of guess
        # is the same as the index
        # of the secretNum,
        # give the clue of Fermi.

        # The index in this context is the nth number of the digit

        # So, if the first digit of the guess number
        # is the same as the first digit of the secret number,
        # then the clue 'Fermi' is added

        elif guess[i] in secretNum:
            clues.append('Pico')

    # The 'in' keyword is literal
    # If x is in y, do that

    # If the nth digit is in the secret number, 'Pico is added'

    if len(clues) == 0:
        return 'Bagels'

    else:
        clues.sort()

        # Sort the clues into alphabetical order so that
        # The user does not know what digit is in the right or wrong place

        return ' - '.join(clues)

    # Makes a single string from the list of values


# If the program is run (instead of imported), run the game:

if __name__ == '__main__':
    main()
