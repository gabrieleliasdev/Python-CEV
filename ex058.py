"""
  058 - Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
  Só que agora o jogador vai tentar advinhar até acertar, mostrando no final quantos palpites foram necessários
  para vencer.
"""
from random import randint

bot = randint(0, 10)
print(bot)
print("The computer was thinker a number from 0 to 10. ")

hint = int(input("Hint: "))
qt_hint = 1

while hint != bot:
  if hint < bot:
    hint = int(input("More... I'm sorry, but it wasn't this time. Try again: "))
  else:
    hint = int(input("Less... I'm sorry, but it wasn't this time. Try again: "))
  qt_hint += 1

print("Congratulations! You got it right after {} attempts.".format(qt_hint))

