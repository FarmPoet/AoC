p1 = p2 = 0
for entry in open('2.txt').read().split()[:]:
    l, w, h = map(int, entry.split('x'))
    p1 += 2*l*w + 2*w*h + 2*h*l + min(l*w, l*h, h*w)
    p2 += min(2*l+2*w, 2*l+2*h, 2*h+2*w) + l*w*h
    
p1, p2