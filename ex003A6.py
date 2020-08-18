n1 = input('Type a value: ')
print(type(n1))

n2 = int(input('Type a value: '))
print(type(n2))

n3 = int(input('Type another value: '))

s = n2+n3

print(f'The sum of {n2} + {n3} is = {s}')

print('The sum of {} + {} is = {}'.format(n2,n3,s))
