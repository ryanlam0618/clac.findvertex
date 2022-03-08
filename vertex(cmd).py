from fractions import Fraction
A = int(input('A:'))
B = int(input('B:'))
C = int(input('C:'))

Δ = B ** 2 - 4 * A * C
h = (-B / (2 * A))
print('Δ=' + str(Δ))
print('H=', Fraction(h))
h = Fraction(h)
k = (C - (A * (h ** 2)))
print('K=', Fraction(k))
k = Fraction(k)
print('vertex=', '(', h, ",", k, ')', sep='')
