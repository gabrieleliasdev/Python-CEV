print("{:=^20}".format(" 'Exempla 01' "))
for c in range(1, 6):
  print("Hello")
print("End")
print("{:=^20}".format(" 'Exempla 02' "))
for c in range(0, 6):
  print(c)
print("End")
print("{:=^20}".format(" 'Exempla 03' "))
for c in range(6, 0, -1):
  print(c)
print("End")
print("{:=^20}".format(" 'Exempla 04' "))
for c in range(0, 6, 2):
  print(c)
print("End")
print("{:=^20}".format(" 'Exempla 05' "))
n = int(input("Type a number: "))
for c in range(0, n+1):
  print(c)
print("End")
print("{:=^20}".format(" 'Exempla 06' "))
i = int(input("Start: "))
f = int(input("End: "))
s = int(input("Step: "))
for c in range(i, f+1, s):
  print(c)
print("End")
print("{:=^20}".format(" 'Exempla 07' "))
s = 0
for c in range(0,4):
  n = int(input("Type a value: "))
  s += n
print(f"Print s: {s}")
print("The sum of all values was {}".format(s))
print(f"{s[0]}")
s1 = s[0]
print(s1)
