# Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('\nType your full name:\n>>> ')).strip().title()

n1 = n.split()

print('\nYour first name {} and your last name {}.\n'.format(n1[0], n1[-1]))
