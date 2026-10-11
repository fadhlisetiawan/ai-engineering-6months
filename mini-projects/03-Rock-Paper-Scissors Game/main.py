import random


def play_game():
    # 1. Initialize choices and starting scores
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    cpu_score = 0

    # 2. Game loop runs until one player reaches a score of 3
    while player_score < 3 and cpu_score < 3:
        # Get player input and format it
        player_choice = input("Your choice? ").strip().lower()

        # Option to quit the game
        if player_choice == "exit":
            print("\n=== Game Over ===")
            break

        # Validate input (ensure it is rock, paper, or scissors)
        if player_choice not in choices:
            print("Invalid choice! Please type rock, paper, or scissors.\n")
            continue

        # CPU makes a random choice from the list
        cpu_choice = random.choice(choices)
        print(f"CPU chose: {cpu_choice}")

        # 3. Evaluate winning rules for each round
        if cpu_choice == player_choice:
            print("It's a tie!\n")

        elif (
            (cpu_choice == "rock" and player_choice == "scissors")
            or (cpu_choice == "paper" and player_choice == "rock")
            or (cpu_choice == "scissors" and player_choice == "paper")
        ):
            print("CPU wins!\n")
            cpu_score += 1

        else:
            print("You win!\n")
            player_score += 1

        # Display current score board
        print(f"Current Score -> Player: {player_score} | CPU: {cpu_score}\n")

    # 4. Determine the final winner of the game
    if player_score == 3:
        print("You win the game!\nGood job!")

    if cpu_score == 3:
        print("CPU wins the game!\nTry again!")


def main():
    # Display welcome message and instructions
    print("=== Welcome to Rock-Paper-Scissors ===")
    print("Type 'rock', 'paper', 'scissors' or type 'exit' to quit the game.\n")

    # Run the game
    play_game()


# Main program entry point
if __name__ == "__main__":
    main()