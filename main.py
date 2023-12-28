import random

coin = input("Choose heads or tails (1 for heads, 0 for tails): ")

headsortails = random.randint(0,1)

coin = headsortails
if coin == 1:
  print ("The coin landed on heads")
else: 
  print ("The coin landed on tails")