# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$ 0,50 por KM para viagens de até 200km.
# ... e R$ 0,45 para viagens mais longas.

s = '-=-'*20
km = int(input(f'\n{s}\nInforms the distance of your trip in kilometers:\n>>> km '))

if km <= 200:
  print(f'\n{s}\nBeing equal to or less than 200km your trip will cost R$ 0,50 for km.\n'
                 'Your will pay: R$ {:.2f}\n'.format(km*0.50))
else:
  print(f'\n{s}\nBeing over 200km your trip will cost R$ 0,45 for km.\n'
                 'You will pay: R$ {:.2f}\n'.format(km*0.45))
