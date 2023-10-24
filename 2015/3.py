c = 'v^<>'
d1 = list(open('3.txt').read()[::-1])
d2 = d1.copy()

pos1 = [0,0]
h = {'[0, 0]':1}
while(d1):
    x = c.index(d1.pop())
    pos1[(x&2)>>1] += 1 if x&1 else -1
    h[str(pos1)] = 1
p1 = len(h)

pos1 = [0,0]
pos2 = pos1.copy()
h = {'[0, 0]':1}
while(d2):
    x = c.index(d2.pop())
    y = c.index(d2.pop())
    pos1[(x&2)>>1] += 1 if x&1 else -1
    pos2[(y&2)>>1] += 1 if y&1 else -1
    h[str(pos1)] = 1
    h[str(pos2)] = 1
p2 = len(h)

p1, p2
