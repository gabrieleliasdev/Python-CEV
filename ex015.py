va = float(input('\nType the daily car rental amount:\n>>> R$ '))

km = float(input('\nType the value for Km driven:\n>>> R$ '))

r = float(input('\nHow many days rented?\n>>> '))

d = float(input('\nHow many Km did you drive?\n>>> '))

pag = (va * r) + (km * d)

print('\nYou rented for {} days and traveled {:.2f}km, you will pay R${:.2f}\n'.format(r,d,pag))
