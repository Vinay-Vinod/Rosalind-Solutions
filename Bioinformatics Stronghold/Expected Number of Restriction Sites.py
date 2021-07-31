from collections import Counter

data = """
10
AG
0.25 0.5 0.75
"""

data = data.split()
n = int(data[0])
s = data[1]
a = list(map(float, data[2:]))

c = Counter(s)
AT = c['A'] + c['T']
GC = c['G'] + c['C']

b = []
for i, j in enumerate(a):
    p = (((1 - j)/2)**AT)*((j/2)**GC)*(n - len(s)+1)
    b.append('%0.3f' % p)

print(*b, sep=' ')
