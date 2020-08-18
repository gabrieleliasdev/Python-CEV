print(f"\n{'Exemple 01':=^40}\n")

lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
#del(lanche)
for c in lanche:
    print(c, end=" ")

print('\n\n{:=^40}\n'.format("Exemple 02"))

lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
for cont in range(0, len(lanche)):
    print(lanche[cont], end=' ')

print('\n\n{:=^40}\n'.format("Exemple 03"))

lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
for cont in range(0, len(lanche)):
    print(lanche[cont], cont, end=' ')

print('\n\n{:=^40}\n'.format("Exemple 04"))

lanche = 'Hambúrguer', 'Suco', 'Pizza', 'Pudim'
for pos, c in enumerate(lanche):
    print(c, pos, end=" ")

print('\n\n{:=^40}\n'.format("Exemple 05"))

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)
print(sorted(c))
print(c.count(5))
print(c.index(8))

