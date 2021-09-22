from Bio import pairwise2
from Bio import SeqIO
from Bio.SubsMat.MatrixInfo import blosum62

s = 'PLEASANTLY'
t = 'MEANLY'

a = pairwise2.align.globalds(s, t, blosum62, -5, -5)
print(pairwise2.format_alignment(*a[0]))
