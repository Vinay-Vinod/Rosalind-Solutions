import itertools       

n = 3                                            
s = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']  

perm = itertools.product(s, repeat=n)   

for i, j in enumerate(list(perm)):                
    permutation = ''                              
    for item in j:                                
        permutation += str(item)   
        
    print(permutation)
