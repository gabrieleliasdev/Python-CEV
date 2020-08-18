"""
  060 - Faça um programa que leia um número qualquer e mostre o seu fatorial. Ex.: 5! = 5x4x3x2x1 = 120
"""
"""
n = int(input("Type a number: "))

f = n*(n-1)*(n-2)*(n-3)*(n-4)

print(f)
"""
"""
from math import factorial

n = int(input("Type a number: "))
f = factorial(n)
print("The factorial of {} is {}".format(n,f))
"""
from time import sleep

print("-=-"*10)

n = int(input("\nType a number: "))

c = n

f = 1

print(f"\nCalculantig {n}!\n")
sleep(2)

while c > 0:
  print(f"{c}", end="")
  print(" x " if c > 1 else " = ", end="")
  f *= c
  c -= 1

print(f)
