import random
import time

question = input('If you want to roll the dice, key in the letter y: ')
response = str("y")
done = str("n")



def dice():
  while response == "y":
    no = random.randint(1,6)
    print(no)
    time.sleep(3)
    question = input('If you want to roll the dice again, key in the letter y. If not, key in letter n: ')
    if question == done:
      break
  print('Thanks for playing')
  

if question == response:
    dice()