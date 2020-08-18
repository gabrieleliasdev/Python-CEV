"""044 - Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
  condição de pagamento:
  - à vista dinheiro/cheque: 10% de desconto.
  - à vista no cartão: 5% de desconto.
  - em até 2x no cartão: preço normal
  - 3x ou mais no cartão: 20% de juros"""

v = float(input("\nInform the value of the product: R$ "))

print("\nSelect the paymente method:\n[a] Cash or Check\n[b] Cash on the Card"
      "\n[c] On the Card for 02 times\n[d] On the Card for 3 times or more")

p = str(input(">>> ")).strip().lower()

a = v - (v*10/100)
b = v - (v*5/100)
c = v
d = v + (v*20/100)

if p == 'a':
  print("\nProduct value: {:.2f} | Payment method: Cash or Check | Discount: 10% | Will pay: {:.2f}\n".format(v,a))

elif p == 'b':
  print("\nProduct value: {:.2f} | Payment method: Cash on the Card | Discount: 5% | Will pay: {:.2f}\n".format(v,b))

elif p == 'c':
  print("\nProduct value: {:.2f} | Paymente method: On the Card for 02 times | No discount | Will pay: {:.2f}\n".format(v,c))

elif p == 'd':
  print("\nProduct value: {:.2f} | Paymente method: On the Card for 3 times or more | Increase tax 20% | Will pay: {:.2f}\n".format(v,d))

else:
  print("\nChoose one of the options. Try again!\n")
