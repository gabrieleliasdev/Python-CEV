"""036 - Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
  O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
  *Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo
  será negado."""

vh = float(input('\nWhat is the value of the house you want to buy? R$ '))

vs = float(input("\nYour salary? R$ "))

vp = float(input("\nHow many times do you want to pay this amount? "))

ws = vs * 30 / 100

wp = vh/vp

yp = vp/12

print("\nValue of House: R$ {:.2f} | Your Salary: R$ {:.2f} | Number of times: {}\n"
      "\n30% margin of salary: R$ {:.2f} | Monthly fee: R$ {:.2f} | Financing in year: {}"
      .format(vh,vs,vp,ws,wp,yp))

if wp <= ws:
  print("\nAnalysis approved! Monthly payments do not commit more than 30% of your salary.\n")

else:
  print("\nAnalysis failed. Monthly payments commit more than 30$ of your salary.\n")
