from math import sin, cos, tan, radians

a = float(input('\nType the angle you want:\n>>> '))

s = sin(radians(a))

c = cos(radians(a))

t = tan(radians(a))

print('\nThe is Sine: {:.2f} | Cosine: {:.2f} | Tangent: {:.2f}\n'.format(s,c,t))
