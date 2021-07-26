# For some reason this only works in Python 2, since it starts to differ around the 15th place
# Use this online ide --> https://www.jdoodle.com/python-programming-online/

from math import factorial
from collections import Counter

s = 'AUGCUUC'

c = dict(Counter(s))

au = factorial(max(c['A'], c['U'])) / factorial(max(c['A'], c['U']) - min(c['A'], c['U']))
gc = factorial(max(c['G'], c['C'])) / factorial(max(c['G'], c['C']) - min(c['G'], c['C']))

print(int(au * gc))
