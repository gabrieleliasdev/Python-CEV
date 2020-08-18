for c in range(1, 10):
  print(c, end=" ")
print("\nEnd")

c = 1
while c < 10:
  print(c, end=" ")
  c = c + 1
print("\nEnd")

n = 1
while n != 0:
  n = int(input("Type a value: "))
print("\nEnd")

n = 1
even = odd = 0
while n != 0 :
  n = int(input("Type a value: "))
  if n != 0:
    if n % 2 == 0:
      even += 1
    else:
      odd += 1
print("Qt. even {} | Qt. odd: {}".format(even, odd))
