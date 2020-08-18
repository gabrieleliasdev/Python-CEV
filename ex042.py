"""042 - Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
  - Equilátero: todos os lados iguais.
  - Isóceles: dois lados iguais.
  - Escaleno: todos os lados diferentes."""

s = '-=-'*20
print(s)
print('Analisador de Triângulos')
print(s)
r1 = float(input('First segment: '))
r2 = float(input('Second segment: '))
r3 = float(input('Third segment: '))



if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
  print(f'\nThe above segments "can" form a Triangle!\n{s}\n')

  if r1 == r2 == r3:
    print("Is Equilátero!")

  elif r1 == r2 or r1 == r3 or r2 == r3:
    print("Is Isóceles!")

  elif r1 != r2 != r3 != r1:
    print("Is Escaleno")


else:
  print(f'\nThe above segments "cannot" form a Triangle.\n{s}\n')
