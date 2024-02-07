## User input & Control flow
# Rock Paper Scissors
import sys
import random
from enum import Enum


def rps(name="PlayerOne"):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # print(RPS(2))
        # print(RPS.ROCK)
        # print(RPS['ROCK'])
        # print(RPS.ROCK.value)

        playerChoice = input(
            f"\n{name}, please enter...\n1 for Rock,\n2 for Paper, or \n3 for Scissors:\n\n"
        )

        # user input is string so need to convert into int
        player = int(playerChoice)

        # typing anything besides 1,2,3 will
        if playerChoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_rps()

        computerChoice = random.choice("123")
        computer = int(computerChoice)

        print(f"\n{name}, you chose {str(RPS(player)).replace("RPS.", "").title()}.")
        print(f"Python chose {str(RPS(computer)).replace("RPS.", "").title()}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🎉 {name}, You win!"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🎉 {name}, You win!"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🎉 {name}, You win!"
            elif player == computer:
                return "😲 Tie game!"
            else:
                python_wins += 1
                return f"🐍 Python wins! Sorry {name}...😢"

        game_result = decide_winner(player, computer)
        print(game_result)

        # parent function scope variable and game count print
        nonlocal game_count
        game_count += 1
        print(f"\nGame count: {(game_count)}")
        print(f"\n{name}'s winning count: {(player_wins)}")
        print(f"\nPython's winning count: {(python_wins)}")

        # if anything is typed besides y or q it will keep asking
        print(f"\nPlay again {name}?")
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
            sys.exit(f"Bye {name}!👋")

    return play_rps


# play will hold the play_rps funtion return
# play = rps()
# play()


# Adding command line arguments for the user
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a Personal Gaming Experience"
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="Name of the person playing the game.",
    )

    args = parser.parse_args()

    # making the file as a module
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
