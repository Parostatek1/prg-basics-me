###
# A program that calculates the length of the diagonal
# of a rectangle with sides a and b.
#
import math
a = input ('podaj przyprostokatna a: ')
b = input('podaj przyprostokatna b : ')
boka = int(a)
bokb = int(b)
diagonal = math.sqrt(boka**2 + bokb**2)
print(diagonal)