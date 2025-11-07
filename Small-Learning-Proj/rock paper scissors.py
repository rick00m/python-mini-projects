import random

def get_choices():
    player_choice = input("Enter your choice (rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    while player_choice not in options:
        player_choice = input("Invalid choice. Please enter rock, paper, or scissors: ")
    computer_choice = random.choice(options)
    choices = { "player": player_choice, "computer": computer_choice }
    return choices

def check_win(player, computer):
    print(f"You chose {player}, CPU chose {computer}")
    if player == computer:
        return "Tie game!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock wins, Flawless victory."
        else:
            return "Covered up, You have fallen."
    elif player == "paper":
        if computer == "rock":
            return "Paper wins, Flawless victory."
        else:
            return "Sliced, You have fallen."
    elif player == "scissors":
        if computer == "paper":
            return "Cut through your enemy, Flawless victory."
        else:
            return "Smashed, You have fallen."

player_score = 0
cpu_score = 0
ties = 0

while True:
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)

    if "Flawless victory" in result:
        player_score += 1
    elif "fallen" in result:
        cpu_score += 1
    else:
        ties += 1

    print(f"Scores -> You: {player_score}, CPU: {cpu_score}, Ties: {ties}")

    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay != "yes":
        print("Thanks for playing! Final scores:")
        print(f"You: {player_score}, CPU: {cpu_score}, Ties: {ties}")
        break






