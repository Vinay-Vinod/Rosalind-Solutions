from math import comb

n, m = 1685, 747
s = 0

for i in range(m, n + 1):
    s += comb(n,i)
    
print(s % 1000000)
