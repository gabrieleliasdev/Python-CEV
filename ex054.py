"""
  054 - Crie um programa que leia o ano de nascimento de sete pessoas. No final,
  mostre quantas pessoas ainda não atingiram a maior idade e quantas jão são maiores.
  """

from datetime import date

today = date.today().year
tl = 0
tm = 0
for person in range(1,8):

  born = int(input("What year was the {}ª person born? ".format(person)))

  age = today - born

  if age >= 18:
    tl += 1

  else:
    tm += 1

print("We had {} people of age and {} minors.".format(tl, tm))
