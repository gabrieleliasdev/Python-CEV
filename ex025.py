# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

n = str(input('\nType your full name, please:\n>>> ')).strip().title()

print('\nThis name {} "Silva"\n'.format("Silva" in n))
