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
            return "Paper wins, Flawless victory"
        else:
            return "Sliced, You have fallen."
    elif player == "scissors":
        if computer == "paper":
            return "Cut through your enemy, Flawless victory"
        else:
            return "Smashed, You have fallen."
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
    



