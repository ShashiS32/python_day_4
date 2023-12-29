import random

while True:

  choices = ["Rock" , "Paper" , "Scissors"]
  
  player_choice = input("Rock, Paper, or Scissors?: ")
  
  
  AIRandom = random.randint(0,2)
  
  AIChoice = choices[AIRandom]
  
  if player_choice.lower == "rock":
    if AIChoice == "Rock":
      print ("You tied with the AI!")
    elif AIChoice == "Paper":
      print ("You lost, the AI chose paper!")
    else:
      print("You won, the AI chose scissors!")
  elif player_choice.lower == "paper":
    if AIChoice == "Rock":
      print ("You won, the AI chose rock!")
    elif AIChoice == "Paper":
      print ("You tied with the AI!")
    else:
      print("You lost, the AI chose scissors!")
  elif player_choice.lower =="scissors":
    if AIChoice == "Rock":
      print ("You lost, the AI chose rock!")
    elif AIChoice == "Paper":
      print ("You won, the AI chose paper!")
    else:
      print("You tied with the AI!")
  
  else:
    print("Invalid choice!")
  
  play_again = input("Do you want to play again? (yes/no): ")
  if play_again.lower() == "no":
      print("Thanks for playing!")
      break
  
  
  