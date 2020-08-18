"""
    Exercício Python 080
    Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
    já na posição correta de inserção (sem usar o sort()).
    No final, mostre a lista ordenada na tela.
"""
lst = []

for c in range(0,5):
    v = int(input(f"Digite valor númerico » "))
    if c == 0 or v > lst[-1]:
        lst.append(v)
        print("Adicionado ao final da lista...")
    else:
        pos = 0
        while pos < len(lst):
            if v <= lst[pos]:
                lst.insert(pos, v)
                print(f"Adicionado no index '{pos}' da lista")
                break
            pos += 1

print('-='*30)
print(f"Os valores digitados em ordem foram {lst}")

