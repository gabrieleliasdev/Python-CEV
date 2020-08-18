""" 078
    Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
    No final, mostre qual foi o maior e o menor valor digitado as suas respectivas posições na lista.
"""
print(f"\n{'Resolução Parcial':=^40}\n")
from textwrap import dedent

lst = list(int(input(f"Digite o {i+1}º numero: ")) for i in range(5))

for c, v in enumerate(lst):
        print(dedent(f"""
                        Lista » {lst}
                        O maior valor é {max(lst)} e está nos index's {lst.index(max(lst))}
                        O menor valor é {min(lst)} e está nos index's {lst.index(min(lst))}
                    """))
        break

print(f"\n{'Resolução Completa':=^40}\n")

lst = list(int(input(f"Digite o {i+1}ª número: ")) for i in range(5))

print(f"\nO maior valor é {max(lst)} e está nos index's ", end="")
for i, v in enumerate(lst):
    if v == max(lst):
        print(f"'{i}' ", end="")

print(f"\n\nO menor valor é {min(lst)} e está nos index's ", end="")
for i, v in enumerate(lst):
    if v == min(lst):
        print(f"'{i}' ", end="")

print("\n")