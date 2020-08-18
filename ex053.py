"""053 - Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços"""

ph = str(input("Type a pharse: ")).strip().lower()
sp = ph.split()
jp = "".join(sp)
iv = ""
ivf = jp[::-1]

for c in range(len(jp) -1, -1, -1):
  iv += jp[c]

if iv == jp:
  print("\nIt's a Palíndromo!")

else:
  print("\nIt is not a Palíndromo!")

print(f"\nph = '{ph}'")
print(f"\nsp = '{sp}'")
print(f"\njp = '{jp}'")
print(f"\niv = '{iv}'")
print(f"\nivf = '{ivf}'")
print(f"\njp + iv = '{jp, iv}'")
print("\nEnd")
