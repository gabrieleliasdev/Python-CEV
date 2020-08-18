# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

n = float(input('Type a value in meters and it will be converted to centimeters and millimeters.\n>>> '))

# centimeters
cm = n*100

# milimeters
mm = n*1000

print('>>> {} in "centimeters" is {:.0f}cm, and in "millimeters" it is {:.0f}mm.'.format(n,cm,mm))
