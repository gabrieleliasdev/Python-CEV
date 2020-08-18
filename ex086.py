"""
    Exercício Python #086 - Matriz em Python
    Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
    No final, mostre a matriz na tela, com a formatação correta.
"""
lst = [[], [], []]

for i in range(9):
    i = int(input(f"Type {i+1}ª value » "))
        
    if len(lst[0]) <= 2:
        lst[0].append(i)
    
    elif len(lst[1]) <= 2:
        lst[1].append(i)
    
    else:
        lst[2].append(i)

print(f"\nBelow is the matrix in correct formation:\n » {lst[0]}\n » {lst[1]}\n » {lst[2]}\n")

print("\n » Resolution by Professor Gustavo Guanabara ")

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"\nDigite um valor para [{l}, {c}]: "))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end="")
    print()