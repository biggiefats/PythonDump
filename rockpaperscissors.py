import random

from colorama import Fore

cw = 0
pw = 0

while True:

    r = 'Rock'
    s = 'Scissors'
    p = 'Papers'

    choices = ['R', 'P', 'S']
    computer = random.choice(choices)
    player = None

    a = [Fore.YELLOW + "It's a tie!" + Fore.RESET,
         Fore.RED + "Computer wins!" + Fore.RESET,
         Fore.GREEN + "Player wins!" + Fore.RESET]

    while player not in choices:

        # While the player's choice (input) is not in the list (choice),

        player = input("Please enter your choice: Rock, Paper or Scissors [R,P,S]: ").upper()

        # .upper() turns the input into an upper case input

        if player == computer:
            print(f'''
            Computer choice: {computer}
            Player choice: {player}
                    {a[0]}
''')

        elif player == choices[0]:

            if computer == choices[1]:
                cw += 1
                print(f'''
                Computer choice: {p}
                Player choice: {r}
                {a[1]}
''')

            elif computer == choices[2]:
                pw += 1
                print(f'''
                Computer choice: {computer}
                Player choice: {player}
                {a[2]}
                ''')

        elif player == choices[1]:
            if computer == choices[2]:
                cw += 1
                print(f'''
                Computer choice: {computer}
                Player choice: {player}
                {a[1]}
''')

            if computer == choices[0]:
                pw += 1
                print(f'''
                Computer choice: {computer}
                Player choice: {player}
                {a[2]}
''')

        elif player == choices[2]:

            if computer == choices[0]:
                cw += 1
                print(f'''
                Computer choice: {computer}
                Player choice: {player}
                {a[1]}
''')

            if computer == choices[1]:
                pw += 1
                print(f'''
                Computer choice: {computer}
                Player choice: {player}
                {a[2]}
''')

    print("The computer has won {} times whereas you have won {} times in this session.".format(cw, pw))
    
    play_again = input("Do you want to play again? Y for Yes, N for No: ").upper()

    if play_again != 'Y':
        break

print("Session terminated.")
