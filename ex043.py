"""043 - Desenvolva um lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status,
  de acordo com a tabela abaixo:
  - Abaixo de 18.5: Abaixo do peso
  - Entre 18.5 e 25: Peso ideal
  - 25 até 30: Soprepeso
  - 30 até 40: Obsidade
  - Acima de 40: Obsidade mórbida"""

w = float(input("\nType your weigth: "))

h = float(input("\nType your heigth: "))

imc = w / (h ** 2)

print("\nYour IMC: {:.2f}".format(imc))

if imc < 18.5:
  print("\nUnder weigth")

elif imc <= 25:
  print("\nIdeal weigth")

elif imc < 30:
  print("\nOverweigth")

elif imc < 40:
  print("\nObesity")

else:
  print("\nMorbid obesity")
