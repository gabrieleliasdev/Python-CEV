"""045 - Crie um programa que faça o computador jogar Jokenpô com você."""

from random import randint
from time import sleep

g = ("Scissors", "Paper", "Rock")

bot = randint(0, 2) # or bot = choice(g)

print("\nChoose between:\n[0] Scissors\n[1] Paper\n[2] Rock\n")

u = int(input(">>> "))

print("\nJO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!\n")
sleep(1)

print('-=-'*10)
print("You chose '{}' | Bot chose '{}'".format(g[u],g[bot]))
print('-=-'*10)

if bot == 0:

  if u == 0:
    print("A tie")

  elif u == 1:
    print("You lost")

  elif u == 2:
    print("You won!!")

  else:
    print("Invalid option")

elif bot == 1:

  if u == 0:
    print("You won!")

  elif u == 1:
    print("A tie")

  elif u == 2:
    print("You lost")

  else:
    print("Invalid option")

elif bot == 2:

  if u == 0:
    print("You lost")

  elif u == 1:
    print("You won!!")

  elif u == 2:
    print("A tie")

  else:
    print("Option invaled")

else:
  print("Invalid option")
