# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário
# tentar descobrir qual foi o número escolhido pelo computadorpygame.examples.aliens.main()
# O programa deverá escrever na tela se o usuário venceu ou perdeupygame.examples.aliens.main()

from random import randint

bot = randint(0, 5)
print('-=-' * 20)
print("I'll think of a number between 0 to 5... try to find out!")
print('-=-' * 20)
n = int(input('What number did I think of? Good luck!\n>>> '))
if n == bot:
  print('\nCongratulations! You are lucky\n')
else:
  print("\nWon! I thought of {} and not {}\n".format(bot, n))


