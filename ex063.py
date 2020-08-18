"""
    Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos
    de uma Sequência de Fibonacci. Ex.: 0 → 1 → 2 → 3 → 5 → 8
"""
"""
print("-"*30)
print("Fibonacci Sequence")
print("-"*30)
n = int(input("How many Fibonacci sequence numbers do you want? "))
t1 = 0
t2 = 1
print("~"*30)
print(f"{t1} → {t2}", end="")

cont = 3

while cont <= n:
    t3 = t1 + t2
    print(f' → {t3}', end="")
    t1 = t2
    t2 = t3
    cont += 1

print('\nEnd')
"""
Nant = 1
Fibonacci = 0

n = int(input('Digite um número:(Este vai ser o nº de elementos da sequência) '))

while n >= 0:
    print('{} → '.format(Fibonacci), end='')
    Fibonacci = Fibonacci + Nant
    #1 - 0 + 1 = 1
    #2 - 1 + 0 = 1
    #3 - 1 + 1 = 2
    #4 - 2 + 1 = 3
    #5 - 3 + 2 = 5
    #6 - 5 + 3 = 8
    #7 - 8 + 5 = 13
    Nant = Fibonacci - Nant
    #1 - 1 - 1 = 0
    #2 - 1 - 0 = 1
    #3 - 2 - 1 = 1
    #4 - 3 - 1 = 2
    #5 - 5 - 2 = 3
    #6 - 8 - 3 = 5
    n -= 1
    #10 -= 1 == 9
    # 8
print('FIM')