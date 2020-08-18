from random import choice

a1 = str(input('\nName of student 1:\n '))
a2 = str(input('Name of student 2:\n '))
a3 = str(input('Name of student 3:\n '))
a4 = str(input('Name of student 4:\n '))

lista = [a1, a2, a3, a4]

choosing = choice(lista)

print('The chosen student is {}'.format(choosing))
