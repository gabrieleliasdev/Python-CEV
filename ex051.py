"""051 - Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros
  termos dessa progressão."""

fn = int(input("Type the first number: "))
r = int(input("Ratio: "))
t = fn + (10-1) * r #décimo termo de uma progressão aritmética
for c in range(fn, t + r, r):
  print(f"{c}", end=" -> ")

print("End")
