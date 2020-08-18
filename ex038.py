"""038 - Escreva um programa que leia 02 números inteiros e compare-os, mostrando na tela uma mensagem:
  - O primeio valor é maior. - O segundo valor é maior - Não exite valor maior, os dois são iguais."""

v1 = int(input("Type two values:\nFirst value: "))
v2 = int(input("Second value: "))


if v1 > v2:
  print("The first value is largest")

elif v2 > v1:
  print("The second value is largest")

elif v1 == v2:
  print("Values are equal")

else:
  print('Erro')
