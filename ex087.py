"""
    Exercício Python #087 - Mais sobre Matriz em Python
    Aprimore o desafio anterior, mostrando no final: 
        A) A soma de todos os valores pares digitados.
        B) A soma dos valores da terceira coluna.
        C) O maior valor da segunda linha.
"""
lst = [[], [], []]
se = sc = 0

for i in range(9):
    i = int(input(f"Type {i+1}ª value » "))
        
    if len(lst[0]) <= 2:
        lst[0].append(i)
    
    elif len(lst[1]) <= 2:
        lst[1].append(i)
    
    else:
        lst[2].append(i)

    if i % 2 == 0:
        se += i

for i in range(3):
    sc += lst[i][2]

print(f"\nBelow is the matrix in correct formation:\n » {lst[0]}\n » {lst[1]}\n » {lst[2]}")

print(f"\na) Sum of even values » '{se}'")

print(f"\nb) Sum of the values in the third column is » '{sc}'")

print(f"\nc) The highest value of the second line » '{max(lst[1])}'")        

print("\n » Resolution by Professor Gustavo Guanabara")