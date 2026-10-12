import math
h = input('input height [m]: ')
hg = float(h)
d = round(3.57 * math.sqrt(hg),3)
print(d, 'km')