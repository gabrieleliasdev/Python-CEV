""" 073
    Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
    na ordem de colocação. Depois mostre:
    a) Os 5 primeiros times.
    b) Os últimos 4 colocados.
    c) Times em ordem alfabética.
    d) Em que posição está o time da Chapecoense.
"""
print("\n{:=^50}\n".format("Exercise 73"))

lst = "Flamengo", "Corinthians", "Bragantino-SP", "Palmeiras", "Atlético-GO", "Goiás"

print("The top 6 in the 2020 Brazilian Championship table:")
for c in lst:
    print(c)

print(f"\nThe fist 5 teams » {lst[0:5]}\n")

print(f"The last 4 placed » {lst[-4:]}\n")

print("Alphabetical list:")
s = sorted(lst)
for c in s:
    print(c)

print(f"\nThe Corinthians are in '{lst.index('Corinthians')+1}ª' position.")

print("\nEnd\n")

