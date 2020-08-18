# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date

s = '-=-'*20

y = int(input(f'\n{s}\nType the year and I will tell you if it is leap or not.\n'
                       'If you want to consult the current year, type "0":\n>>> Year '))

if y == 0:
  y = date.today().year
if y % 4 and y % 100 != 0 or y % 400 == 0: #Divisivel por 04, não pode ser divisivel por 100, ou divisivel por 400
  print(f'\nThis year {y} is leap!\n{s}\n')
else:
  print(f'\nThis year {y} is not leap.\n{s}\n')
