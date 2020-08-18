import math

num = int(input('\nType a number:\n>>> '))
root = math.sqrt(num)
print('\nThe square root of {} is equal to {:.2f}.'.format(num, root))

# math.ceil - Arredondar pra cima
print('\nThe square root of {} is equal to {}.'.format(num, math.ceil(root)))

# math.floor - Arredondar pra baixo
print('\nThe square root of {} is equal to {}.'.format(num, math.floor(root)))

