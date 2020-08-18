""""
    056 - Desenvolva um programa que leia o nome, idade e sexo de 04 pessoas. No final do programa, mostre:
    a) A média de idade do grupo.
    b) Qual é o nome do homem mais velho.
    c) Quantas mulheres têm menos de 20 anos.
"""
lst = []
sum_age = 0
largest_ageM = 0
older_nameM = ''
qt_W20 = 0

for x in range(1, 5):
  print(f'----- {x}ª Person -----')
  name = str(input(f"Name: ")).strip().title()
  age = int(input(f"Age: "))
  gender = str(input(f"Gender [M/F]: ")).strip().upper()

  # sum of age
  sum_age += age

  # man + years old
  if x == 1 and gender in 'M':
    largest_ageM = age
    older_nameM = name

  if gender in 'M' and age > largest_ageM:
    largest_ageM = age
    older_nameM = name

  # woman < 20 years old
  if gender in "F" and age < 20:
    qt_W20 += 1

  lst += name, age, gender, '→' ,

print(f'\n{lst}\n')

ma = (sum_age) / 4
print("\nThe avegare age of this group is {:.1f}".format(ma))
print("\nThe oldest man is {} years old and is called {}.".format(largest_ageM, older_nameM))
print("\nWe have {} women under the age of 20.".format(qt_W20))

