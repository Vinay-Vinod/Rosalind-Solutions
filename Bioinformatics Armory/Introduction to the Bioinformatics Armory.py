from collections import Counter

s = 'AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC'
val = {'A':0, 'C':0, 'G':0, 'T':0}

c = Counter(s)

for i in c:
    val[i] = c[i]

print(*val.values(), sep = ' ')
