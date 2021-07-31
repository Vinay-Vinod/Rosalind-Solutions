from collections import Counter 

def mrm(n, x, s):
    c = Counter(s)

    AT = c['A'] + c['T']
    GC = c['G'] + c['C']

    s_prob = (((1 - x) / 2)**AT) * (((x) / 2)**GC)
    prob = 1 - (1 - s_prob)**n
    print('%0.3f' % prob)

n = 90000
x = 0.6
s = 'ATAGCCGA'

mrm(n, x, s)
