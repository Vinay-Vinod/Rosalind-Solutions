n = 10
x = {1, 2, 3, 4, 5}
y = {2, 8, 5, 10}

u = []
for i in range(1, n+1):
    u.append(i)
u = set(u)

print(x | y)
print(x & y)
print(x - y)
print(y - x)
print(u^x)
print(u^y)
