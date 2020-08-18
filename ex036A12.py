n = str(input("What's your name? ")).strip().title()

if n == "Gabriel":
  print("Beautiful name.")
elif n == 'Pedro' or n == 'João' or n == 'Tiago':
  print("Name of disciples.")
elif n in "Bruno, Breno, Fernado":
  print("Cool name.")
else:
  print("Your name is common.")

print("Have a good blessed day!")
