# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$ 7,00 por cada KM acima do limite.

s = '-=-' * 20

vu = int(input(f'{s}\nReports car speed:\n>>> Km/h '))

if vu > int(80):
  print(f'{s}\nYou were fined for exceeding 80km/h.',
  '\nIt will cost you R$ 7,00 for km exceeded.',
  '\nYou will pay: R$ {:.2f}\n'.format((vu - 80) * 7))
else:
  print(f'{s}Very vell! Within the permitted speed.\n')
