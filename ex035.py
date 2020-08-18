s = '-=-'*20
print(s)
print('Analisador de Triângulos')
print(s)
r1 = float(input('First segment: '))
r2 = float(input('Second segment: '))
r3 = float(input('Third segment: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print(f'\nThe above segments "can" form a Triangle!\n{s}\n')

else:
  print(f'\nThe above segments "cannot" form a Triangle.\n{s}\n')
