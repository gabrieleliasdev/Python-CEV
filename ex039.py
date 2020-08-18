"""039 - Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
  - Se ele ainda vai se alistar ao serviço militar.
  - Se é a hora de se alistar.
  - Se já passou do tempo do alistamento
  Seu programa também deverá mostrar o tempo que falta ou que passou do prazo."""

from datetime import date

t = date.today().year

b = int(input('Type your year of birth: '))

o = t - b

print("Who was born in {} is {} years old in {}".format(b,o,t))

if o == 18:
  print("You have to enlist immediately")

elif o < 18:
  s = 18 - o
  print("{} years until the enlistment".format(s))
  y = t + s
  print("Your enlistment will be in {}".format(y))

elif o > 10:
  s = o -18
  print("Your time for enlistment has passed. Was {} years ago.".format(s))
  y = t - s
  print("His enlistment was in {}".format(y))
