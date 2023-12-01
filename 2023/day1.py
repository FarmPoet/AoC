import re

n = {'o1e':'one', 't2o':'two', 't3e':'three', 'f4r':'four', 'f5e':'five',
        's6x':'six', 's7n':'seven', 'e8t':'eight', 'n9e':'nine'}

def getN(d): return(sum([int(j[0] + j[-1]) for j in [re.findall(r'\d', i) for i in d]]))

d = open("i1.txt").read().split()
p1 = getN(d)
for k, v in n.items(): d = [re.sub(v, k, i) for i in d]
p2 = getN(d)
           
p1, p2
