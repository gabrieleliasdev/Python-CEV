"""
    Crie um programa que leia o nome e o preço de vários produtos.
    O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
    A) qual é o total gasto na compra.
    B) quantos produtos custam mais de R$1000.
    C) qual é o nome do produto mais barato.
"""
from textwrap import dedent

title = "Registration Product"
title1 = "End of Program"

lst = []

sm = q = s = cont = 0

n_s = ' '

while True:
    print('- = '*16)
    print(f"{title:^64}")
    print('- = '*16)

    n = str(input("\nInform name » ")).strip().title()
    v = float(input("Inform value » R$ "))
    
    lst += [n, v]
    sm += v
    cont += 1
    
    if v > 1000:
        q += 1
    
    if cont == 1 or v < s:
        s = v
        n_s = n
    
    res = ' '
    while res not in 'YN':
        res = str(input("\nDo you wish cont? [Y/N] » ")).strip().upper()[0]
    if res != 'Y':
        break

print(f"{title1:-^64}")
print(f"\nThis is the shopping list » {lst}")

print(dedent(f"""
            | Total purchase » R${sm:.2f}\n
            | Quantity of products over » '{q}'\n
            | '{n_s}'' was the cheapest product, costing only R${s:.2f}
            """))
