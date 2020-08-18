# Faça um algortimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

v = float(input('\nWhat is the price of the product?\n>>> R$ '))

d = float(input('\nHow much discount will I aplly:\n>>> '))

vf = v-(v*d/100)

print('\nIn cash, we aplly {:.0f}% discount, the product will cost R$ {:.2f}.\n'.format(d,vf))
