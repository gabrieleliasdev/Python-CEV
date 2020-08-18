"""
  057 - Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado,
  peça a digitação novamente até ter um valor correto.
"""
"""
n = ''

while n != " ":
  n = str(input("Whats your gender [F/M]? ")).strip().upper()
  if n == "M" or n == "F":
    print(f"Your gender is {n}")
    exit()

print("\nEnd")
"""

gender = str(input("Inform your gender [M/F]: ")).strip().upper()[0]
while gender not in 'MF':
  gender = str(input("Invalid data. Please, inform your gender again [M/F]: ")).strip().upper()[0]
print(f"Sex '{gender}' registered successfully.")

