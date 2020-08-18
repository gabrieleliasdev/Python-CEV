su = 0
qt = 0

for c in range(1, 7):
  n = int(input("Type the {} value: ".format(c)))
  if n % 2 == 0: # Se o número é divisivel por 02 e verificar se a divisão é igual a 0
    su += n
    qt += 1

print("You type {} even numbers | Their sum is: {}".format(qt,su))
