from Bio.Seq import Seq

dna = "TCAATGCATGCGGGTCTATATGCAT"
dna = Seq(dna)

for i in range(len(dna)):
    for j in range(i, len(dna)):
        d_temp = dna[i:j+1]
        r_temp = d_temp.reverse_complement()
        if len(d_temp) >=4 and len(d_temp) <=12:
            if d_temp == r_temp:
                print(i+1, len(d_temp))
            





