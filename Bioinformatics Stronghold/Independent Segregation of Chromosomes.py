import numpy as np

n = 5
p = 0.5

pr = 0
a = []
for k in range(2*n, 0, -1):
    pr += np.math.factorial(2*n)/(np.math.factorial(k)*np.math.factorial(2*n-k)) * np.power(p,k)*np.power(1-p, 2*n-k)
    a.append(round(np.log10(pr), 3))
    
for i in a[::-1]:
    print(i, end=' ')
