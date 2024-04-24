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
