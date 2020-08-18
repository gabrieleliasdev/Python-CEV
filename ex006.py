# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('>>> '))

#doube
d = n*2

#triple
t = n*3

#square root
sr = n**(1/2)

print('The chosen number was: {}\nYour double is: {}\nYour triple is: {}\n...and its square root is: {:.2f}'.format(n,d,t,sr))
