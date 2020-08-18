"""037 - Escreva um programa que leia um número inteiro qualquer e pela para o usuário escolher qual será a
  base de conversão: 1) para binário 2) octal 3) hexadecimal"""

n = int(input("\nType the number you want to convert:\n>>> "))

print("""\nChoose the option for conversion:
[a] Convert to Binary
[b] Convert to Octal
[c] Convert to Hexadecimal\n""")

oc = str(input(">>> ")).strip().lower()

if oc == 'a':
  print("\nThis value {} convert to Binary becomes {}\n".format(n, bin(n)[2:]))

elif oc == 'b':
  print("\nThis value {} convert to Octal becomes {}\n".format(n, oct(n)[2:]))

elif oc == 'c':
  print("\nThis valou {} convert to Hexadecimal becomes {}\n".format(n, hex(n)[2:]))

else:
  print("\nChoose one of the options above.\n")
