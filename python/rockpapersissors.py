import random
import time

print("chose rock (1), paper (2), sissors (3)")
while True:
  try:
    word = int(input())
  except ValueError as e:
    print("enter a number not a letter")
    continue
  break
  
computerchose = random.randint(1, 3)

if computerchose == 1:
  if word == 1:
    print("Tied the game!")
  if word == 2:
    #working on it
