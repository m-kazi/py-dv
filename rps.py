## User input & Control flow
# Rock Paper Scissors
import sys
import random
from enum import Enum

# Constant variable are always uppercase


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    # print(RPS(2))
    # print(RPS.ROCK)
    # print(RPS['ROCK'])
    # print(RPS.ROCK.value)

    playerChoice = input(
        "\nEnter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"
    )

    # user input is string so need to convert into int
    player = int(playerChoice)

    # typing anything besides 1,2,3 will
    if playerChoice not in ["1", "2", "3"]:
        print("You must enter 1, 2, or 3.")
        return play_rps()

    computerChoice = random.choice("123")
    computer = int(computerChoice)

    print("\nYou chose " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Python chose " + str(RPS(computer)).replace("RPS.", "") + ".\n")

    if player == 1 and computer == 3:
        print("🎉 You win!")
    elif player == 2 and computer == 1:
        print("🎉 You win!")
    elif player == 3 and computer == 2:
        print("🎉 You win!")
    elif player == computer:
        print("😲 Tie game!")
    else:
        print("🐍 Python wins!")

    # if anything is typed besides y or q it will keep asking
    print("\nPlay again?")
    while True:
        playagain = input("\nY for Yes or \nQ for quit \n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        play_rps()
    else:
        print("\n🎉🎉🎉🎉")
        print("Thank you for playing!\n")
        sys.exit("Bye! 👋")


play_rps()
