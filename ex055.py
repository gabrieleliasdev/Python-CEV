"""
  055 - Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior
  e o menor peso lidos.
"""
"""
w1 = float(input(f"Type the weight of 1ª person: Kg "))
w2 = float(input(f"Type the weight of 2ª person: Kg "))
w3 = float(input(f"Type the weight of 3ª person: Kg "))
w4 = float(input(f"Type the weight of 4ª person: Kg "))
w5 = float(input(f"Type the weight of 5ª person: Kg "))

wt = [w1, w2, w3, w4, w5]
owt = sorted(wt)

print(f"\nThis are the weights shown: {wt}")
print(f"\nThey are in order: {owt}")
print(f"\nThis is the smallest weight '{owt[0]}kg' followed by the largest '{owt[-1]}kg'\n")
"""
"""
larg = 0
small = 0

for weigth in range(1, 6):
  w = float(input(f"Type the weight of {weigth}ª person: Kg "))

  if weigth == 1:
    larg = w
    small = w

  else:

    if w > larg:
      larg = w

    if w < small:
      small = w

print(f"\nThis is the smallest weight '{small}kg' followed by the largest '{larg}kg'\n")
"""
lst = []
for weigth in range(1, 6):
  w = float(input(f"Type the weight of {weigth}ª person: Kg "))
  lst += [w]

print(lst)
print("This largest weigth is:", max(lst))
print("This smallest weigth is:", min(lst))
