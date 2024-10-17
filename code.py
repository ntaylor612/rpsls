"""
             project: rpsls.py
              author: Natalie Taylor <ntaylor2701004@woonsocketschools.com>
        date written: 10/8/24
 
    description: Rock, Paper, Scissors, Lizard, Spock for 2 players
"""

print("Welcome to Rock Paper Scissors Lizard Spock!")
print("""
        The rules are simple:
        rock beats scissors,
        rock beats lizard,
        spock beats rock,
        paper beats rock,
        paper beats spock,
        lizard beats paper,
        scissors beats paper,
        scissors beats lizard,
        spock beats scissors, and
        lizard beats spock.
""")


print()
playerOne = input("Player one whats your name? ")
playerTwo = input("Player two whats your name? ")
score1 = score2 = 0
isPlaying = True
print()

while isPlaying is True:
    print("""
            For this game, youll need to insert:
            R for rock
            P for paper
            S for scissors
            L for lizard
            SP for spock
     """)
    weaponOne = input("Player one, choose your weapon: ")
    weaponTwo = input("Player two, choose your weapon: ")

    print()
    if weaponOne == weaponTwo :
            # Draw
    if weaponOne == "R":
        if weaponTwo == "R":
            print("Its a draw!")
        elif weaponTwo == "S":
            print("Rock beats Scissors", playerOne, "wins!")
            score1 = score1 + 1
        elif weaponTwo == "L":
            print("Rock beats Lizard", playerOne, "wins!")
            score1 = score1 + 1
        elif weaponTwo == "SP":
            print("Spock beats Rock", playerTwo, "wins!")
            score2 = score2 + 1
        else :
            print("Paper beats Rock", playerTwo, "wins!")
            score2 = score2 + 1

     elif weaponOne == "S":
        if weaponTwo == "S":
            print("Its a draw!")
        elif weaponTwo == "R":
            print("Scissors beats Rock", playerTwo, "wins!")
            score2 = score2 + 1
        elif weaponTwo == "L":
            print("Scissors beats Lizard", playerOne, "wins!")
            score1 = score1 + 1
        elif weaponTwo == "SP":
            print("Spock beats Scissors", playerTwo, "wins!")
            score2 = score2 + 1
        else :
            print("Scissors beats Paper", playerOne, "wins!")
            score1 = score1 + 1

    elif weaponOne == "P":
        if weaponTwo == "P":
            print("Its a draw!")
        elif weaponTwo == "R":
            print("Paper beats Rock", playerOne, "wins!")
            score1 = score1 + 1
        elif weaponTwo == "L":
            print("Lizard beats Paper", playerTwo, "wins!")
            score2 = score2 + 1
        elif weaponTwo == "SP":
            print("Paper beats Spock", playerOne, "wins!")
            score1 = score1 + 1
        else :
            print("Scissors beats Paper", playerTwo, "wins!")
            score2 = score2 + 1

   elif weaponOne == "L":
        if weaponTwo == "L":
            print("Its a draw!")
        elif weaponTwo == "R":
            print("Rock beats Lizard", playerTwo, "wins!")
            score2 = score2 + 1
        elif weaponTwo == "P":
            print("Lizard beats Paper", playerOne, "wins!")
            score1 = score1 + 1
        elif weaponTwo == "SP":
            print("Lizard beats Spock", playerOne, "wins!")
            score1 = score1 + 1
        else :
            print("Scissors beats Lizard", playerTwo, "wins!")
            score2 = score2 + 1

    else : # weaponOne == "SP":
        if weaponTwo == "SP":
            print("Its a draw!")
        elif weaponTwo == "R":
            print("Spock beats Rock", playerOne, "wins!")
            score1 = score1 + 1
        elif weaponTwo == "P":
            print("Paper beats Spock", playerTwo, "wins!")
            score2 = score2 + 1
        elif weaponTwo == "L":
            print("Lizard beats Spock", playerTwo, "wins!")
            score2 = score2 + 1
        else :
             print("Scissors beats Lizard", playerTwo, "wins!")
             score2 = score2 + 1

    print()
    print(f"{playerOne}, your score is {score1} \n")
    print(playerTwo, "score is", score2)

    ask = input("Would you like to play another round? (Type Yes Or No): ")
    if ask != "Yes":
        isPlaying = False
# End of While loop

print()
if score1 > score2:
    print(f"{playerOne} wins!")
else:
    print(playerTwo, "wins!")
