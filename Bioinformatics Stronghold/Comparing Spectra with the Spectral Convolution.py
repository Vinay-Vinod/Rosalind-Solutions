from collections import Counter

x = '186.07931 287.12699 548.20532 580.18077 681.22845 706.27446 782.27613 968.35544 968.35544'
y = '101.04768 158.06914 202.09536 318.09979 419.14747 463.17369'

x, y = list(map(float, x.split())), list(map(float, y.split()))

mdiff = []
for i in x:
    for j in y:
        diff = round(i-j, 5)
        mdiff.append(diff)
        
c = Counter(mdiff).most_common(1)

print(c[0][1])
print(c[0][0])
