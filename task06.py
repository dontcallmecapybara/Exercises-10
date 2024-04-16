from solution import RomanNumber_6


a = RomanNumber_6('XI')
b = RomanNumber_6('VII')
c = a + b
print(c)
d = RomanNumber_6('XII')
print(c - d)
e = RomanNumber_6('XXXIV')
f = e * a
print(f)
print(f / RomanNumber_6('II'))
g = f / b
print(g.rom_value)
print(f // b)
print(f % b)
print(RomanNumber_6('II') ** RomanNumber_6('X'))
a -= b
print(a)
b += RomanNumber_6('XX')
print(b)
b /= RomanNumber_6('III')
print(b)
b *= a
print(b)
b /= RomanNumber_6('X')
print(b)
e //= RomanNumber_6('X')
print(e)
e %= RomanNumber_6('II')
print(e)
