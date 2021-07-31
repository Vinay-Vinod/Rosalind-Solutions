from Bio import Entrez

data = '''
Anthoxanthum
2003/7/25
2005/12/27
'''

data = data.split()
handle = Entrez.esearch(db="nucleotide", term=('{}[Organism] AND {}:{}[PDAT]').format(data[0], data[1], data[2]))
record = Entrez.read(handle)

print(int(record["Count"]))
