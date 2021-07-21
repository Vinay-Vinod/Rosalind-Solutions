import requests

def parse(d):
    lst = []
    for i in d:
        url = "http://www.uniprot.org/uniprot/" + i + ".fasta"
        page = requests.get(url)
        all_txt = page.text
        result = "".join([i for i in all_txt if not i.isdigit()])
        info = result.split("SV=")
        lst.append(info[-1].strip())

    return lst

def find(s):
    s = ''.join(s.split())
    temp = []
    for i in range(len(s)-4):
        if s[i] == 'N' and s[i+1] != 'P' and (s[i+2] == 'S' or s[i+2] == 'T') and s[i+3] != 'P':
            temp.append(i+1)
    return temp

d = """
P01046_KNL1_BOVIN
P02974_FMM1_NEIGO
P12763_A2HS_BOVIN
Q83I57
B5FPF2
P05113_IL5_HUMAN
Q67JS9
P10493_NIDO_MOUSE
C0QUK8
Q2GBA3
P0C5G9
Q9CE42
P29460_I12B_HUMAN
Q14ID0
"""

d = d.split()
protein = []
protein = parse(d)

index = 0

for item in protein:
    res = find(item)
    
    if len(res) > 0:
        print(d[index])
        print(*res, sep= ' ')
        
    index += 1
