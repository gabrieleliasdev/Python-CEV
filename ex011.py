# Faça um programa que leia a largura e a altura de uma parade em metros,
# calcule a sua área e a quantidade de tinta necessária para pinta-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

print('This program will tell you, how many liters of paint you will need to paint the area you want.')

h = float(input('Type the height of the wall in meters:\n>>> '))

w = float(input('Type the width of the wall in meters?\n>>> '))

m = h*w

lp = 2

mp = m/lp

print('\nThe area to be painted is {}m². You will need {}m² of paint to paint it.\n'.format(m,mp))
