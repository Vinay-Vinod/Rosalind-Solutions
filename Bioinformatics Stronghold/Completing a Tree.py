data = '''
10
1 2
2 8
4 10
5 9
6 10
7 9
'''

data = list(map(int, data.split()))
new = [[data[0]]]

for i in range(1, len(data), 2):
    new.append(data[i:i+2])

start = new[0][0]
edges = new[1:]

print(start - len(edges) - 1)
