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
    print("tied the game!")
  if word == 2:
    print("player won the game!")
  if word == 3:
    print("computer won the game!")
if computerchose == 2:
  if word == 1:
    print("computer won the game!!")
  if word == 2:
    print("tied the game!")
  if word == 3:
    print("player won the game!")
if computerchose == 3:
  if word == 1:
    print("player won the game!")
  if word == 2:
    print("computer won the game!")
  if word == 3:
    print("tied the game!")

