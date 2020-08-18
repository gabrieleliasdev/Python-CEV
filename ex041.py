"""041 - A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
  e mostre sua categoria, de acordo com a idade:
  - Até 9 anos: Mirin
  - Até 14 anos: Infantil
  - Até 19 anos: Junior
  - Até 20 anos: Sênior
  - Acima: Master """

from datetime import date

t = date.today().year

b = int(input("\nInforms the date of birth: "))

age = t-b

print("\nAthlete age: {}\n".format(age))

if age <= 9:
  print("Mirin")

elif age <= 14:
  print("Infantil")

elif age <=19:
  print("Junior")

elif age <= 20:
  print("Sênior")

elif age > 20:
  print("Master")
