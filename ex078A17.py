"""
    del lanche[3]
    lanche.pop(3)
    lanche.remove("pizza")
    lanche.pop()
    if "pizza" in lanche:
        lanche.remove("pizza")
    t = tuple(range(4,11))
    l = list(range(4,11))
    print(b.sort())
    print(b.sort(reverse=True))
    print(len(b))
"""

lst = [2,5,9,1]
print(f"\nLista original » {lst}")

print(f"\n{'Exemple 01':=^40}\n")

lst[2] = 3
print(f"Substituindo valores em lista 'n[2] = 3' » {lst}")

print(f"\n{'Exemple 02':=^40}\n")

lst.append(7)
print(f"Adicionando item a lista 'lst.append(7)' » {lst}")

print(f"\n{'Exemple 03':=^40}\n")

lst.insert(2,0)
print(f"Inserindo item a lista em uma posição específica 'lst.insert(2,0)' » {lst}")

print(f"\n{'Exemple 04':=^40}\n")

lst.sort()
print(f"Colocando a lista em ordem 'lst.sort()' » {lst}")

print(f"\n{'Exemple 05':=^40}\n")

lst.sort(reverse=True)
print(f"Colocando a lista em ordem reversa 'lst.sort(reverse=True)' » {lst}")

print(f"\n{'Exemple 06':=^40}\n")

lst.pop(2)
print(f"Retirando item específico da lista através de sua 'posição' 'lst.pop(2)' » {lst}")

print(f"\n{'Exemple 07':=^40}\n")

lst.remove(5)
print(f"Procura do ínicio da lista até a 1ª ocorrencia com o 'valor' especifiado 'lst.remove(5)' » {lst}")

print(f"\n{'Exemple 08':=^40}\n")

lst = []
lst.append(5)
lst.append(9)
lst.append(4)

for c, v in enumerate(lst):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Cheguei ao final da lista.")

print(f"\n{'Exemple 09':=^40}\n")

lst = []
for cont in range(0, 5):
    lst.append(int(input("Type a number: ")))

for c, v in enumerate(lst):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Cheguei ao final da lista.")

print(f"\n{'Exemple 10':=^40}\n")

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print("Como clonar uma lista! Up!!!")
print(f"Lista A: {a}")
print(f"Lista B: {b}\n")
