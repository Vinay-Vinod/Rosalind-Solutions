import itertools
import regex as re

data = '''
CTTCGAAAGTTTGGGCCGAGTCTTACAGTCGGTCTTGAAGCAAAGTAACGAACTCCACGG
CCCTGACTACCGAACCAGTTGTGAGTACTCAACTGGGTGAGAGTGCAGTCCCTATTGAGT
TTCCGAGACTCACCGGGATTTTCGATCCAGCCTCAGTCCAGTCTTGTGGCCAACTCACCA
AATGACGTTGGAATATCCCTGTCTAGCTCACGCAGTACTTAGTAAGAGGTCGCTGCAGCG
GGGCAAGGAGATCGGAAAATGTGCTCTATATGCGACTAAAGCTCCTAACTTACACGTAGA
CTTGCCCGTGTTAAAAACTCGGCTCACATGCTGTCTGCGGCTGGCTGTATACAGTATCTA
CCTAATACCCTTCAGTTCGCCGCACAAAAGCTGGGAGTTACCGCGGAAATCACAG
'''

data = ''.join(data.split())

start = 'ACGT'      
perm = itertools.product(start, repeat=4)

kmers = []
for i, j in enumerate(list(perm)):
    kmer = ''
    for item in j:
        kmer += str(item)
    kmers.append(kmer)

occ = []

def counter(full, sub):
    return len(re.findall(sub, full, overlapped=True))

for i in range(len(kmers)):
    occ.append(counter(data, kmers[i]))
    
print(*occ, sep = ' ')
