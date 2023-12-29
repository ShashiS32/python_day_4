import random

choices = ["Rock" , "Paper" , "Scissors"]

player_choice = input("Rock, Paper, or Scissors? (1 for Rock, 2 for Paper, 3 for Scissors): ")

AIRandom = random.randint(0,3)

AIChoice = choices[AIRandom]

if player_choice == "1":
  if AIChoice == 0:
    print ("You tied with the AI!")
  elif AIChoice == 1:
    print ("You lost, the AI chose paper!")
  else:
    print("You won, the AI chose scissors!")
elif player_choice == "2":
  if AIChoice == 0:
    print ("You won, the AI chose rock!")
  elif AIChoice == 1:
    print ("You tied with the AI!")
  else:
    print("You lost, the AI chose scissors!")
else:
  if AIChoice == 0:
    print ("You lost, the AI chose rock!")
  elif AIChoice == 1:
    print ("You won, the AI chose paper!")
  else:
    print("You tied with the AI!")