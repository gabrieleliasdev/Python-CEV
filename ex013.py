# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

s1 = float(input('\nType the current salary:\n>>> '))
adc = float(input('\nType the raise you want to give:\n>>> '))
s2 = s1+(s1*adc/100)

print("\nJoão's current salary is R$ {:.2f} and will increase by {}%. The salary will be R$ {:.2f}.\n".format(s1,adc,s2))
