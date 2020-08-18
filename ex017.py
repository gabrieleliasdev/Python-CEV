# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

from math import hypot

co = float(input('\nCompression of Opposite leg:\n>>> '))

ca = float(input('\nCompression of Adjacent leg:\n>>> '))

hy = hypot(co, ca)

#Hypotenuse = (co ** 2 + ca ** 2) ** (1/2)
print('Opposite leg: {} | Adjacent leg: {} | Compression of the Hypotenuse: {:.2f}'.format(co, ca, hy))
