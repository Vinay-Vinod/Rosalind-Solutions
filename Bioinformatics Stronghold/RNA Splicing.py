from Bio.Seq import Seq

def parse(data):
    s = []
    ros_loc = []
    data = data.split()
    
    i = 0
    while i < len(data) - 1:
        if ">" in data[i]:
            ros_loc.append(i)
        i += 1

    i = 0
    while i < len(ros_loc) - 1:
        temp_list = data[ros_loc[i] + 1 : ros_loc[i + 1]]
        temp_string = ""
        for letter in temp_list:
            temp_string += letter
        s.append(temp_string)
        i += 1

    temp_list = data[ros_loc[i] + 1 :]
    temp_string = ""
    for letter in temp_list:
        temp_string += letter
    s.append(temp_string)
    
    return s

data = '''
>Rosalind_10
ATGGTCTACATAGCTGACAAACAGCACGTAGCAATCGGTCGAATCTCGAGAGGCATATGGTCACATGATCGGTCGAGCGTGTTTCAAAGTTTGCGCCTAG
>Rosalind_12
ATCGGTCGAA
>Rosalind_15
ATCGGTCGAGCGTGT
'''

s = parse(data)
dna = s[0]
removes = s[1:]

for item in removes:
    dna = dna.replace(item, '')
    
dna = Seq(dna)
print(dna.translate())

