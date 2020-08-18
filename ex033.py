# Faça um programa que leia 03 números e mostre qual é o maior e qual é o menor.

n1 = int(input('\nType three numbers and I will inform you which is the smallest and the largest among them:'
              '\n\n>>> Fisrt number: '))

n2 = int(input('>>> Second number: '))

n3 = int(input('>>> Third number: '))

n = [n1, n2, n3]

r = sorted(n)

print('\nThese are the numbers you chose {}.\n'
      'Now, they are in order {} | The smallest is {} | The largest is {}\n'
      .format(n, r, r[0], r[-1]))

print('-=-'*20)
smallest = n1
if n2 < n1 and n2 < n3:
  smallest = n2
elif n3 < n1 and n3 < n2:
  smallest = n3

largest = n1
if n2 > n1 and n2 > n3:
  largest = n2
elif n3 > n1 and n3 > n2:
  largest = n3

print(f' The smallest: {smallest} | The largest: {largest}')
