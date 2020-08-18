"""
  059 - Crie um programa que leia dois valores e mostre um menu na tela:
  [1] somar | [2] multiplicar | [3] maior | [4] novos números [5] sair do programa
  Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import sleep
v1 = int(input("First value: "))
v2 = int(input("Second value: "))

choice = 0

while choice != 5:
  choice = int(input("\nChoose from these options:\n[1] Add\n[2] Multiply\n"
                     "[3] Larger\n[4] New numbers\n[5] Exit the program\n>>> "))
  print("Processing...")
  sleep(2)
  vt = f"{v1} and {v2}"
  if choice == 1:
    print(f"The sum of {vt} = {v1 + v2}")

  elif choice == 2:
    print(f"The mutilplication of {vt} = {v1 * v2}")

  elif choice == 3:
    print(f"This is largest number:", max(v1, v2))

  elif choice == 4:
    print("Return to the beginning.")
    v1 = int(input("First value: "))
    v2 = int(input("Second value: "))

  elif choice == 5:
    print("See you later!")

  else:
    print("Invalid option. Try again!")

  print("-=-"*10)
  sleep(3)

print("Thanks. Bye!")
