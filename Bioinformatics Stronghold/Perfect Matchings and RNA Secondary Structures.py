from math import factorial           
from Bio.Seq import Seq

s = Seq('CUCAAGACCUGUAGUACAGAGUCUAACAACGUUAGGUGCGUUGGGACUUCCCCCAGCGACGCUGAGCUUGGC')                            
                        
AU = 0                                     
GC = 0                                     
for item in s:                        
    if item == 'A':                          
        AU += 1                            
    elif item == 'G':                        
        GC += 1                            

m = factorial(AU) * factorial(GC)  
print(m)   
