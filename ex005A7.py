name = str(input('>>> '))
print('>{}!'.format(name))
print('>{:20}!'.format(name))
print('>{:>20}!'.format(name))
print('>{:^20}!'.format(name))
print('>{:=^20}!'.format(name))

n1 = int(input('Type a value: '))
n2 = int(input('Type another value: '))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('Sum: {} | Multiplication: {} | Division: {}'.format(s,m,d))
print('Entire Division: {} | Exponentialization: {}'.format(di,e))
print('Division: {:.2f}'.format(d))

print('Sum: {} | Multiplication: {} | Division: {}'.format(s,m,d), end=' | ')
print('Entire Division: {} | Exponentialization: {}'.format(di,e), end=' | ')
print('Division: {:.2f}'.format(d))
