# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
#  e mostre quantos Dólares ela pode comprar.

n = float(input('\nHow much money is in your walltet?\n>>>R$ '))

d = 3.27

buy = (n/d)

print('\nWith this value in R$ {:.2f}, you can buy U$$ {:.2f}.\n'.format(n,buy))
