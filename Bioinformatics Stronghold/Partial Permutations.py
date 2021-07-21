def perm(n, k):
    p = 1
    for i in range(k):
        p *= (n - i)
    print(p % 1000000)
    
perm(21, 7)
