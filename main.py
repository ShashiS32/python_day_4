import random

print ("Welcome to the coin simulation, heads = 1, tails = 0")

coin = random.randint(0,1)

if coin == 1:
  print ("The coin landed on heads")
else: 
  print ("The coin landed on tails")