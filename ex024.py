# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

c = str(input(f'\nType the name of a City:\n>>> ')).strip().title()

c1 = c.split(' ')

print('This City {} "Santo" in your name.\n'.format("Santo" in c1 [0]))

# OR

print(c[0:5] == 'Santo')
