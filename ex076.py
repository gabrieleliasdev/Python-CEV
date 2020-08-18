""" 076
    Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
    No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

lst = ("Milk", 3.50,
       "Coffee", 4.00,
       "Bread", 3.00,
       "Açúcar", 2.50)

print(f"\n{'-'*38}")
print(f"{'LISTAGEM DE PREÇO':^40}")
print(f"{'-'*38}\n")
sm = 0

for pos in range(0, len(lst)):
    if pos % 2 == 0:
        print(f"{lst[pos]:.<30}", end=" ")
    else:
        print(f"R${lst[pos]:>5.2f}")
        sm += lst[pos]

lst1 = "Total", sm

for pos in range(0, len(lst1)):
    if pos % 2 == 0:
        print(f"\n{lst1[pos]:.<30}", end=' ')
    else:
        print(f"R${lst1[pos]:>5.2f}")

print(f"{'-'*38}\n")
