from itertools import permutations

def perm(x):
    return list(permutations(range(1, x+1)))

res = perm(3)

print(len(res))
for item in res:
    print(*item, sep=' ')
