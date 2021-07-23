from itertools import permutations

def perm(x):
    r = []
    for i in range(-x, x+1):
        #Can't include 0
        if i != 0:
            r.append(i)
            
    perms = list(permutations(r, x))
    return perms

n = 2
res = [list(x) for x in perm(n)]
new_res = []

#No negative/positive duplicates, ex: 1 & -1
for i in range(len(res)):
    temp = list(map(abs, res[i]))
    dup = (len(temp) != len(set(temp)))
    if dup == False:
        new_res.append(res[i])

print(len(new_res))
for item in new_res:
    print(*item, sep=' ')
