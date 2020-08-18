"""
   Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
   um de cada vez, para cada valor digitado pelo usuário.
   O programa será interrompido quando o número solicitado for negativo.
"""

n = 0

while True:
    n = int(input("Want to konw the multiplication table of which number? » "))
    if n < 0:
        break
    for c in range(0,11):
        print(f"{c:2} x {n} = {c*n}")

print("Thank you and come back often")