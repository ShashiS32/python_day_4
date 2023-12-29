import random

while True:
    choices = ["rock", "paper", "scissors"]

    player_choice = input("rock, paper, or scissors?: ")

    ai_random = random.randint(0, 2)
    ai_choice = choices[ai_random]

    if player_choice.lower() == "rock":
        if ai_choice == "rock":
            print("You tied with the AI!")
        elif ai_choice == "paper":
            print("You lost, the AI chose paper!")
        else:
            print("You won, the AI chose scissors!")
    elif player_choice.lower() == "paper":
        if ai_choice == "rock":
            print("You won, the AI chose rock!")
        elif ai_choice == "paper":
            print("You tied with the AI!")
        else:
            print("You lost, the AI chose scissors!")
    elif player_choice.lower() == "scissors":
        if ai_choice == "rock":
            print("You lost, the AI chose rock!")
        elif ai_choice == "paper":
            print("You won, the AI chose paper!")
        else:
            print("You tied with the AI!")
    else:
        print("Invalid choice!")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() == "no":
        print("Thanks for playing!")
        break
